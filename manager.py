from database.database import Database


class Manager:

    def __init__(self):
        self.db = Database()

    def get_all_phones(self):
        return [{'phone_number': phone['phone_number']} for phone in self.db.find()]

    def block_phones(self, phones):
        valid_json = True
        for phone_doc in phones:
            if 'phone_number' not in phone_doc:
                valid_json = False
                break

        if valid_json:
            for phone_doc in phones:
                # aqui é possível fazer validações

                # validação de número
                if self.__format_phone_number(phone_doc['phone_number']) == "":
                    phone_doc['block_status'] = 'invalid_phone_number'
                    continue

                # validação de duplicidade de phone_number
                if self.db.find_one({'phone_number': self.__format_phone_number(phone_doc['phone_number'])}) is None:
                    self.db.insert({'phone_number': self.__format_phone_number(phone_doc['phone_number'])})
                    phone_doc['block_status'] = 'blocked'
                else:
                    phone_doc['block_status'] = 'duplicated'

            if len(phones) == 1:
                return phones[0]
            else:
                return phones
        else:
            raise KeyError

    def unblock_phones(self, phones):
        valid_json = True
        for phone_doc in phones:
            if 'phone_number' not in phone_doc:
                valid_json = False
                break

        if valid_json:
            for phone_doc in phones:
                # aqui é possível fazer validações

                # validação de existência de phone_number
                if self.db.find_one({'phone_number': self.__format_phone_number(phone_doc['phone_number'])}) is not None:
                    self.db.delete_one({'phone_number': self.__format_phone_number(phone_doc['phone_number'])})
                    phone_doc['block_status'] = 'unblocked'
                else:
                    phone_doc['block_status'] = 'not_found'

            if len(phones) == 1:
                return phones[0]
            else:
                return phones
        else:
            raise KeyError

    def verify_phones(self, phones):
        valid_json = True
        for phone_doc in phones:
            if 'phone_number' not in phone_doc:
                valid_json = False
                break

        if valid_json:
            for phone_doc in phones:

                # aqui é possível fazer validações

                # validação de existência de phone_number
                if self.db.find_one({'phone_number': self.__format_phone_number(phone_doc['phone_number'])}) is not None:
                    phone_doc['block_status'] = 'blocked'
                else:
                    phone_doc['block_status'] = 'not_blocked'

            if len(phones) == 1:
                return phones[0]
            else:
                return phones
        else:
            raise KeyError

    def count(self):
        return len([phone for phone in self.db.find()])

    @staticmethod
    def __format_phone_number(phone_number):
        return ''.join([character for character in phone_number if character.isdigit()])
