from pymongo import MongoClient

from database.database_configs import connection_string, db_name


class Database:

    def __init__(self):
        self.mongo = MongoClient(connection_string).get_database(db_name)
        self.blocked_phones = self.mongo.blocked_phones 

    def insert(self, phones):
        return self.blocked_phones.insert(phones)

    def find(self):
        return [phone for phone in self.blocked_phones.find()]

    def find_one(self, phone):
        return self.blocked_phones.find_one(phone)

    def delete_one(self, phone):
        return self.blocked_phones.delete_one(phone)
