import unittest

from flask import json

from app import api


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = api.test_client()
        phones_setup = json.loads(self.app.get("/phones").get_data())
        if len(phones_setup) > 0:
            response = self.app.delete('/phones', data=json.dumps(phones_setup),
                                       content_type='application/json')
            self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        response = self.app.get('/teste')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {'error': 'Not found'})

    def test_delete_empty_list(self):
        unblocking_phones = []
        response = self.app.delete('/phones', data=json.dumps(unblocking_phones),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # self.assertEqual(json.loads(response.get_data()), unblocking_phones)

    def test_delete_non_existing_phone(self):
        unblocking_phones = [
            {'phone_number': '12345'}
        ]
        response = self.app.delete('/phones', data=json.dumps(unblocking_phones),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data())
        self.assertNotEqual(response_data, unblocking_phones)
        self.assertIn('block_status', response_data)
        self.assertEqual(response_data['block_status'], 'not_found')

    def test_delete_existing_phone(self):
        unblocking_phones = [
            {'phone_number': '12345'}
        ]
        response = self.app.post('/phones', data=json.dumps(unblocking_phones),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.app.delete('/phones', data=json.dumps(unblocking_phones),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data())
        self.assertNotEqual(response_data, unblocking_phones)
        self.assertIn('block_status', response_data)
        self.assertEqual(response_data['block_status'], 'unblocked')

    def test_insert_empty_list(self):
        blocking_phones = []
        response = self.app.post('/phones', data=json.dumps(blocking_phones),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_insert_valid_number(self):
        blocking_phones = [
            {'phone_number': '12345'}
        ]
        response = self.app.post('/phones', data=json.dumps(blocking_phones),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertNotEqual(response_data, blocking_phones)
        self.assertEqual(len(response_data), 2)
        self.assertIn('phone_number', response_data)
        self.assertEqual(response_data['phone_number'], blocking_phones[0]['phone_number'])
        self.assertIn('block_status', response_data)
        self.assertEqual(response_data['block_status'], 'blocked')

    def test_insert_duplicated_number(self):
        blocking_phones = [
            {'phone_number': '12345'},
            {'phone_number': '12345'},
        ]
        response = self.app.post('/phones', data=json.dumps(blocking_phones),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertNotEqual(response_data, blocking_phones)
        self.assertEqual(len(response_data), 2)
        for result in response_data:
            self.assertIn('phone_number', result)
            self.assertEqual(result['phone_number'], blocking_phones[0]['phone_number'])
            self.assertIn('block_status', result)
        self.assertEqual(response_data[0]['block_status'], 'blocked')
        self.assertEqual(response_data[1]['block_status'], 'duplicated')

    def test_verify_existing_number(self):
        blocking_phones = [
            {'phone_number': '12345'}
        ]
        response = self.app.post('/phones', data=json.dumps(blocking_phones),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/verify', data=json.dumps(blocking_phones),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_data(as_text=True))
        self.assertNotEqual(response_data, blocking_phones)
        self.assertEqual(len(response_data), 2)
        self.assertIn('phone_number', response_data)
        self.assertEqual(response_data['phone_number'], blocking_phones[0]['phone_number'])
        self.assertIn('block_status', response_data)
        self.assertEqual(response_data['block_status'], 'blocked')

