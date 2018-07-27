"""API test page"""
import unittest
import json
from datetime import date, datetime
from app.api.api import APP
from app.model.diary import Diary


def create_test_data():
    """method to create testing entries"""
    today_date = str(date.today())
    curent_time = str(datetime.time(datetime.now()))
    entry = Diary(18023171, "Andela", "this is andela")
    dic = {}
    dic["entry_id"] = entry.entry_id
    dic["title"] = entry.title
    dic["date"] = today_date
    dic["time"] = curent_time
    dic["body"] = entry.body
    dic["updated"] = entry.updated
    Diary.entries.append(dic)
create_test_data()


class FlaskTesting(unittest.TestCase):
    """class to test our api"""

    def test_to_create_entry(self):
        """test to create an entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(title="kampala",
                 body="this is my body")), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Entry saved", res.data)

    def test_to_check_duplication_of_data_when_creating_entry(self):
        """test for duplicate data entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
           dict(title="Andela",
                 body="this is andela")), content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Duplicate data,Try again", res.data)    

    def test_to_get_all_entries(self):
        """test to get all entries"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    
    def test_validation_when_creating_entry(self):
        """test to create an entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=1, title="***",
                 body="  ")), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn(b"INCORRECT INPUT, YOU CAN'T SUBMIT EMPTY FIELD OR FIRST CHARACTER SHOULD BE ALPHA NUMERIC", res.data)

    def test_creating_entry_with_wrong_data_format(self):
        """test to create entry with bad data"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data="this is bad data",
                          content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_to_get_single_entry(self):
        """test to get a single entry content"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/18023171',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_for_wrong_url(self):
        """test for wrong url"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/iuut',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_for_id_that_doesnt_exist(self):
        """test to get entry with invalid id"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/2',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_to_update_entry(self):
        """test to update an entry"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/18023171', data=json.dumps(
            dict(title="kampala", body="this is my body updated")),
                         content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"update successful", res.data)

    def test_to_update_entry_that_doesnt_exist(self):
        """test to update entry with invalid id"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data=json.dumps(
            dict(title="kampala", body="this is my body updated")),
                         content_type='application/json')
        self.assertEqual(res.status_code, 404)
        self.assertIn(b"invalid URL, cannot update", res.data)

    def test_to_update_sending_incomplete_parameters(self):
        """test to update entry with invalid id"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data=json.dumps(
            dict(body="this is my body updated")),
                         content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn(b"INVALID OR MISSING DATA FIELDS,CHECK THEM PLEASE", res.data)

    def test_to_update_data_validation(self):
        """test to update entry sending bad data"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data=json.dumps(
            dict(title="***", body=" ")), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn(b"INCORRECT INPUT, YOU CAN'T SUBMIT EMPTY FIELD OR FIRST CHARACTER SHOULD BE ALPHA NUMERIC", res.data)

if __name__ == '__main__':
    unittest.main()
