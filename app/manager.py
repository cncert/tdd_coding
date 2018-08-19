#!coding: utf-8
from app.config import config


class DbManager:
    def __init__(self, db_uri):
        self.db_uri = db_uri

    def db_connect(self):
        try:
            with open(self.db_uri) as db:
                db = db
        except Exception as e:
            db = 'connect fail'
        return db
