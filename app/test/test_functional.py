#!coding: utf-8

import json
import unittest
from pathlib import Path
from ..config import config
from ..manager import add_contactor, list_contactors, update_contactor, search_contactor,\
    delete_contactor
from app.utils import beautify_output


class BaseTest(unittest.TestCase):

    def setUp(self):
        # 不同的函数需要不同的文件读写方式，此处不再统一处理文件打开
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
        response = add_contactor(db=self.db_uri, name=normal_name, phone=normal_phone)
        self.assertEquals(response, 0)

    def test_list_all_contactor(self):
        response = list_contactors(db=self.db_uri)
        self.assertIsInstance(response, list)

    def test_update_contactor_with_empty_info(self):
        response = update_contactor(db=self.db_uri)
        self.assertEquals('Empty contactor', response)

    def test_update_contactor_with_not_fonud_info(self):
        response = update_contactor(db=self.db_uri, update_name='Jack')
        self.assertEquals('Not found contactor to update', response)

    def test_update_contactor_with_wrong_phone(self):
        response = update_contactor(db=self.db_uri, update_name='Tom', update_phone='qq123')
        self.assertEquals('Wrong phone format', response)

    def test_update_contactor_with_correct_info(self):
        response = update_contactor(db=self.db_uri, update_name='Tom', update_phone=13999999999)
        self.assertEquals('update success', response)

    def test_search_contactor_with_correct_info(self):
        response = search_contactor(db=self.db_uri, search_name='Tom')
        self.assertEquals('search down', response[0])

    def test_search_contactor_with_empty_info(self):
        response = search_contactor(db=self.db_uri)
        self.assertEquals('Empty search key', response)

    def test_search_contactor_with_wrong_info(self):
        response = search_contactor(db=self.db_uri, search_name='Jack')
        self.assertEquals('Not found contactor', response)

    def test_delete_contactor_with_correct_info(self):
        response = delete_contactor(db=self.db_uri, delete_name='Tom')
        self.assertEquals('delete success', response)

    def test_delete_contactor_with_empty_info(self):
        response = delete_contactor(db=self.db_uri)
        self.assertEquals('Empty delete key', response)

    def test_delete_contactor_with_wrong_info(self):
        response = delete_contactor(db=self.db_uri, delete_name='Jack')
        self.assertEquals('Not found contactor to delete', response)

    def test_beautify_output_with_list(self):
        test_list = [{u'Tom': u'13013000000'}, {u'Tom': u'13013000000'}, {u'Tom': u'13013000000'}]
        response = beautify_output(test_list)
        self.assertEquals('output list', response)

    def test_beautify_output_with_str(self):
        test_str = 'test data'
        response = beautify_output(test_str)
        self.assertEquals('output str', response)

    def test_beautify_output_with_empty_data(self):
        test_str = ''
        response = beautify_output(test_str)
        self.assertEquals('output null', response)


if __name__ == '__main__':
    unittest.main()