# coding: utf-8

import click
import json
import re
from config import config


class DbManager(object):
    def __init__(self, db_uri):
        self.db_uri = db_uri

    def db_connect(self):
        try:
            with open(self.db_uri) as db:
                db = db
        except Exception as e:
            db = 'connect fail'
        return db


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
DB_URI = config['production'].DB_URI


def verify(phone):
    reg1 = r'^1[3,4,5,7,8][0-9]{9}$'
    reg2 = r'^861[3,4,5,7,8][0-9]{9}$'
    phone = str(phone)
    target_phone = re.findall(reg1, phone)
    target_phone_with_header_86 = re.findall(reg2, phone)
    if target_phone or target_phone_with_header_86:
        return True
    else:
        return False


def add_contactor(**kwargs):
    db = kwargs.get('db', '')
    if not db:
        db = DB_URI
    name = kwargs['name']
    phone = kwargs['phone']
    verify_flag = verify(phone)
    if verify_flag:
        with open(db, 'r') as fr:
            data = json.load(fr)
            data.append({name: phone})
        with open(db, 'w+') as fw:
            data = json.dumps(data, ensure_ascii=False, indent=4)
            fw.write(data)
        return 1
    return 0


def list_contactors(**kwargs):
    pass


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def greet():
    pass


@greet.command()
@click.argument('name')
@click.option('--name','-n', prompt=u'姓名', help=u'要添加的联系人姓名')
@click.option('--phone','-p', prompt=u'电话', type=int, help=u'要添加的电话号码')
def add(**kwargs):
    add_contactor(**kwargs)


@greet.command()
@click.argument('name')
@click.option('--greeting', default='Goodbye', help='word to use for the greeting')
@click.option('--caps', is_flag=True, help='uppercase the output')
def list(**kwargs):
    list_contactors(**kwargs)


if __name__ == '__main__':
    greet()