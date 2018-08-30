#!coding: utf-8

from pathlib import Path


class ProductionConfig:
    BASE_PATH = Path.absolute(Path(__file__).parent.parent)
    DB_URI = str(BASE_PATH / 'mock_data' / 'contactors.db')


class TestsConfig:
    BASE_PATH = Path.absolute(Path(__file__).parent.parent)
    DB_URI = str(BASE_PATH / 'mock_data' / 'mock_for_test.db')


config = {
    'production': ProductionConfig,
    'tests': TestsConfig
}
