# coding: utf-8

import click
import json
import re
from config import config
from utils import parse_db, beautify_output

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
DB_URI = config['production'].DB_URI


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


def verify(phone):
    reg1 = r'^1[3,4,5,7,8][0-9]{9}$'
    reg2 = r'^861[3,4,5,7,8][0-9]{9}$'
    phone = str(phone)
    target_phone = re.findall(reg1, phone)
    target_phone_with_header_86 = re.findall(reg2, phone)
    if target_phone or target_phone_with_header_86:
        return True
    else:
        print 'Add Failed! wrong phone format!'
        return False


def add_contactor(**kwargs):
    db = parse_db(**kwargs)
    name = kwargs['name']
    phone = kwargs['phone']
    verify_flag = verify(phone)
    if not verify_flag:
        return 0
    with open(db, 'r') as fr:
        data = json.load(fr)
        data.append({name: str(phone)})
    with open(db, 'w+') as fw:
        data = json.dumps(data, ensure_ascii=False, indent=4)
        fw.write(data)
    return 1


def list_contactors(**kwargs):
    db = parse_db(**kwargs)
    with open(db, 'r') as fr:
        data = json.load(fr)
    return data


def update_contactor(**kwargs):
    db = parse_db(**kwargs)
    update_name = kwargs.get('update_name', '')
    update_phone = kwargs.get('update_phone', '')
    if not update_name:
        return 'Empty contactor'
    with open(db, 'r') as fr:
        data = json.load(fr)
    keys = [item.keys()[0] for item in data]
    if update_name not in keys:
        return 'Not found contactor to update'
    verify_flag = verify(update_phone)
    if not verify_flag:
        return 'Wrong phone format'
    for item in data:
        if item.keys()[0] == update_name:
            item[update_name] = str(update_phone)
    with open(db, 'w+') as fw:
        data = json.dumps(data, ensure_ascii=False, indent=4)
        fw.write(data)
    return 'update success'


def search_contactor(**kwargs):
    search_result = []
    db = parse_db(**kwargs)
    search_name = kwargs.get('search_name', '')
    if not search_name:
        return "Empty search key"
    with open(db, 'r') as fr:
        data = json.load(fr)
    keys = [item.keys()[0] for item in data]
    if search_name not in keys:
        return 'Not found contactor'
    for item in data:
        if item.keys()[0] == search_name:
            result = search_name + ': ' + item[search_name]
            search_result.append(result)
    return ['search down', search_result]


def delete_contactor(**kwargs):
    db = parse_db(**kwargs)
    delete_name = kwargs.get('delete_name', '')
    if not delete_name:
        return "Empty delete key"
    with open(db, 'r') as fr:
        data = json.load(fr)
    keys = [item.keys()[0] for item in data]
    if delete_name not in keys:
        return 'Not found contactor to delete'
    for item in data:
        if item.keys()[0] == delete_name:
            item.clear()
    while {} in data:
        data.remove({})
    with open(db, 'w+') as fw:
        data = json.dumps(data, ensure_ascii=False, indent=4)
        fw.write(data)
    return 'delete success'


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def greet():
    pass


@greet.command()
@click.argument('name')
@click.option('--name','-n', prompt=u'姓名', help=u'要添加的联系人姓名')
@click.option('--phone','-p', prompt=u'电话', type=str, help=u'要添加的电话号码')
def add(**kwargs):
    add_contactor(**kwargs)


@greet.command()
def list(**kwargs):
    list_data = list_contactors(**kwargs)
    beautify_output(list_data)


@greet.command()
@click.argument('update_name')
@click.option('--update_name','-n', prompt=u'姓名', help=u'要更新的联系人姓名')
@click.option('--update_phone','-p', prompt=u'电话', type=int, help=u'要更新的电话号码')
def update(**kwargs):
    update_data = update_contactor(**kwargs)
    beautify_output(update_data)


@greet.command()
@click.argument('search_name')
@click.option('--search_name',  help=u'要查找的联系人姓名')
def search(**kwargs):
    search_data = search_contactor(**kwargs)
    beautify_output(search_data[1])


@greet.command()
@click.argument('delete_name')
@click.option('--delete_name',  help=u'要删除的联系人姓名')
def delete(**kwargs):
    delete_date = delete_contactor(**kwargs)
    beautify_output(delete_date)


if __name__ == '__main__':
    greet()