#!coding: utf-8

import unittest
from pathlib import Path
from ..config import config


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.db_uri = config['testing'].DB_URI

    def tearDown(self):
        if Path(self.db_uri).exists():
            with open(self.db_uri, 'w') as f:
                f.write('')


class TestContact(BaseTest):

    pass


if __name__ == '__main__':
    unittest.main()