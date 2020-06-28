import unittest

from manager import Manager


class ManagerBlockPhonesTestCase(unittest.TestCase):

    def setUp(self):
        self.manager = Manager()
        self.manager.unblock_phones(self.manager.get_all_phones())
        self.assertEqual(len(self.manager.get_all_phones()), 0)

    def test_empty_phones_list_with_valid_json(self):
        blocking = []
        result = self.manager.block_phones(blocking)
        self.assertEqual(len(result), 0)

    def test_empty_phones_list_with_invalid_json(self):
        blocking = [{'invalid_key': '12345'}]
        self.assertRaises(KeyError, self.manager.block_phones, blocking)
        self.assertEqual(len(self.manager.get_all_phones()), 0)

    def test_one_phone_with_valid_json(self):
        blocking = [
            {'phone_number': '12345'}
        ]
        result = self.manager.block_phones(blocking)
        self.assertEqual(len(result), 2)
        self.assertNotEqual(result, blocking)
        self.assertEqual(result, blocking[0])

    def test_one_phone_with_duplicated_phone_number(self):
        blocking = [
            {'phone_number': '12345'},
            {'phone_number': '12345'}
        ]
        result = self.manager.block_phones(blocking)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(self.manager.get_all_phones()), 1)

        self.assertEqual(result[0], blocking[0])
        self.assertEqual(result[0]['phone_number'], blocking[0]['phone_number'])
        self.assertEqual(result[0]['block_status'], 'blocked')

        self.assertEqual(result[1], blocking[1])
        self.assertEqual(result[1]['phone_number'], blocking[1]['phone_number'])
        self.assertEqual(result[1]['block_status'], 'duplicated')
