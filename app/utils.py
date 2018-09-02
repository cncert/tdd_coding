# encoding: utf-8

from config import config

DB_URI = config['production'].DB_URI


def parse_db(**kwargs):
    db = kwargs.get('db', '')
    if not db:
        db = DB_URI
    return db


def beautify_output(data_list):
    if not data_list:
        print '[]'
        return 'output null'
    if not isinstance(data_list, list):
        print data_list
        return 'output str'
    for item in data_list:
        print item
    return 'output list'