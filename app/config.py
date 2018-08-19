#!coding: utf-8

from pathlib import Path


class ProductionConfig:
    BASE_PATH = Path.absolute(Path(__file__).parent.parent)
    DB_URI = str(BASE_PATH / 'mock_data' / 'contactors.db')


class TestConfig:
    BASE_PATH = Path.absolute(Path(__file__).parent.parent)
    DB_URI = str(BASE_PATH / 'mock_data' / 'test.db')


config = {
    'production': ProductionConfig,
    'testing': TestConfig
}
