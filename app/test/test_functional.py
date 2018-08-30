#!coding: utf-8

import json
import unittest
from pathlib import Path
from ..config import config
from ..manager import add_contactor


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.db_uri = config['tests'].DB_URI

    def tearDown(self):
        if Path(self.db_uri).exists():
            data = [{u'Tom': u'13013000000'}, {u'Tom': u'13013000000'}, {u'Tom': u'13013000000'}]
            data = json.dumps(data, ensure_ascii=False, indent=4)
            with open(self.db_uri, 'w') as f:
                f.write(data)


class TestAddContact(BaseTest):

    def test_add_contactor_with_correct_info(self):
        normal_name = "Tom"
        normal_phone = "13013000000"
        normal_info = {"name": normal_name, "phone":normal_phone}
        response = add_contactor(db=self.db_uri, name=normal_name, phone=normal_phone)
        self.assertEquals(response, 1)

    def test_add_contactor_with_incorrect_info(self):
        normal_name = "Tom"
        normal_phone = "1301300"
        normal_info = {"name": normal_name, "phone":normal_phone}
        response = add_contactor(db=self.db_uri, name=normal_name, phone=normal_phone)
        self.assertEquals(response, 0)


if __name__ == '__main__':
    unittest.main()