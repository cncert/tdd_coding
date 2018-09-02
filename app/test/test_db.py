# encoding: utf-8

from pathlib import Path
import unittest
import json
from app.config import config
from app.manager import DbManager


class DbTest(unittest.TestCase):

    def setUp(self):
        self.db_uri = config['tests'].DB_URI

    def tearDown(self):
        if Path(self.db_uri).exists():
            data = [{u'Tom': u'13013000000'}, {u'Tom': u'13013000000'}, {u'Tom': u'13013000000'}]
            data = json.dumps(data, ensure_ascii=False, indent=4)
            with open(self.db_uri, 'w') as f:
                f.write(data)

    def test_connect_db_with_right_uri(self):
        db_manager = DbManager(self.db_uri)
        db_connector = db_manager.db_connect()
        self.assertIsInstance(db_connector, file)

    def test_connect_db_with_wrong_uri(self):
        db_manager = DbManager('wrong_uri')
        db_connector = db_manager.db_connect()
        self.assertIsInstance(db_connector, str)



if __name__ == '__main__':
    unittest.main()