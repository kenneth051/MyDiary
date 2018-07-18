"""API test page"""
import unittest
import json
from routes import APP

class FlaskTesting(unittest.TestCase):
    """class to test our api"""

    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def test_to_create_entry(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=1, title="kampala", date="4/8/2018", time="3pm",
                  body="this is my body")), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Entry saved", res.data)

    def test_to_get_all_entries(self):
        """test for all get a requests"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)   

    def test_to_duplicate_id(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=1, title="entebbe", date="4/8/2018", time="3pm",
                  body="wrong id")), content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Id has been taken,try again", res.data)

    def test_to_duplicate_data(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data=json.dumps(
            dict(entry_id=2, title="kampala", date="4/8/2018", time="3pm",
                  body="this is my body")), content_type='application/json')
        self.assertEqual(res.status_code, 409)
        self.assertIn(b"Duplicate data,Try again", res.data)

    def test_for_bad_data_entry(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.post('/API/v1/entries', data="this is bad data", content_type='application/json')
        self.assertEqual(res.status_code, 400)   

    def test_to_get_single_entry(self):
        """test for all get a requests"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/1',
                              content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_to_get_none_data_entry(self):
        """test for all get a requests"""
        tester = APP.test_client(self)
        response = tester.get('/API/v1/entries/2',
                              content_type="application/json")
        self.assertEqual(response.status_code, 422)

    def test_to_update_entry(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/1', data=json.dumps(
            dict(title="kampala", body="this is my body updated")), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"updated successfuly", res.data)

    def test_to_update_none_entry(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data=json.dumps(
            dict(title="kampala", body="this is my body updated")), content_type='application/json')
        self.assertEqual(res.status_code, 422)
        self.assertIn(b"invalid Id, cannot update", res.data)

    def test_to_update_bad_data(self):
        """test to create a ride"""
        tester = APP.test_client(self)
        res = tester.put('/API/v1/entries/6', data="this is bad update data", content_type='application/json')
        self.assertEqual(res.status_code, 400)
       

    
if __name__ == '__main__':
    unittest.main()
