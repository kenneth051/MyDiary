"""API test page"""
import unittest
import json
from app import APP

class FlaskTesting(unittest.TestCase):
    """class to test our api"""

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def test_to_create_entry(self):
        """test to create an entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=1, title="kampala", date="4/8/2018", time="3pm",
                  body="this is my body")), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Entry saved", res.data)

    def test_to_get_all_entries(self):
        """test to get all entries"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)   

    def test_to_duplicate_id(self):
        """test for duplicate id"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=1, title="entebbe", date="4/8/2018", time="3pm",
                  body="wrong id")), content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Id has been taken,try again", res.data)

    def test_to_duplicate_data(self):
        """test for duplicate data entry"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=2, title="kampala", date="4/8/2018", time="3pm",
                  body="this is my body")), content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Duplicate data,Try again", res.data)

    def test_for_bad_data_entry(self):
        """test to create entry with bad data"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data="this is bad data", content_type='application/json')
        self.assertEqual(res.status_code, 400)   

    def test_to_get_single_entry(self):
        """test to get a single entry content"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/1',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_for_wrong_url(self):
        """test for wrong url"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/iuut',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)    

    def test_to_get_none_data_entry(self):
        """test to get entry with invalid id"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/2',
                              content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_to_update_entry(self):
        """test to update an entry"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/1', data=json.dumps(
            dict(title="kampala", body="this is my body updated")), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"updated successfuly", res.data)

    def test_to_update_none_entry(self):
        """test to update entry with invalid id"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data=json.dumps(
            dict(title="kampala", body="this is my body updated")), content_type='application/json')
        self.assertEqual(res.status_code, 422)
        self.assertIn(b"invalid Id, cannot update", res.data)

    def test_to_update_bad_data(self):
        """test to update entry sending bad data"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data=json.dumps(
            dict(title="***", body=" ")), content_type='application/json')
        self.assertEqual(res.status_code, 400)
       

    
if __name__ == '__main__':
    unittest.main()
