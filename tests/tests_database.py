import unittest

from database.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        for phone in self.db.find():
            self.db.delete_one(phone)

    def test_get_all_phones(self):
        phones = self.db.find()
        self.assertEqual(len(phones), 0)

    def test_insert_one_phone(self):
        random_phone = [{'phone_number': '12345'}]
        self.db.insert(random_phone)
        self.assertEqual(len(self.db.find()), len(random_phone))

    def test_insert_many_phones(self):
        random_phones = [{'phone_number': str(number)} for number in range(1, 21)]
        self.db.insert(random_phones)
        self.assertEqual(len(self.db.find()), len(random_phones))

    # def test_remove_phones(self):
    #     random_phones = [{'phone_number': str(number)} for number in range(1, 6)]
    #     self.db.insert(random_phones)
    #     all_phones = self.db.find()
    #     self.assertEqual(len(all_phones), len(random_phones))
    #
    #     random_phones_greater_than_other = [{'phone_number': str(number)} for number in range(1, 11)]
    #     self.assertNotEqual(len(all_phones), len(random_phones_greater_than_other))
    #     phones_greater_verified = self.db.verify_phones(random_phones_greater_than_other)
    #     self.assertEqual(len(phones_greater_verified), len(random_phones_greater_than_other))
    #
    #     for phone in self.db.verify_phones(random_phones):
    #         self.assertEqual(phone['status'], 'blocked')
    #     greater_random_phones_verified = self.db.verify_phones(random_phones_greater_than_other)
    #     for i in range(0, len(greater_random_phones_verified)):
    #         phone = greater_random_phones_verified[i]
    #         if i < len(all_phones):
    #             self.assertEqual(phone['status'], 'blocked')
    #         else:
    #             self.assertEqual(phone['status'], 'not_blocked')
