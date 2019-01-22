# -*- encoding: utf-8 -*-
import os
import csv
import logging
import simplejson

DIR = os.path.dirname(__file__)

logging.basicConfig(level=logging.INFO)


def check_dict(items):
    """
    Check if there is a missing key or an invalid value.
    """
    len_keys = None

    for item in items:
        if len_keys is None:
            len_keys = len(item.keys())

        invalid_item = any([
            None in item.keys(),
            None in item.values(),
            '' in item.keys(),
            '' in item.values(),
            len_keys != len(item.keys())
        ])

        if invalid_item:
            raise KeyError('Invalid key or value')


def check_files(file_paths):
    """Check all files from the file_paths list"""
    for file_path in file_paths:
        logging.info('Checking file %s', file_path)
        with open(os.path.join(DIR, file_path), 'r') as f:
            if file_path.endswith('.json'):
                check_dict(simplejson.loads(f.read()))
            elif file_path.endswith('.csv'):
                check_dict(csv.DictReader(f))


if __name__ == '__main__':
    file_paths = [
        '../json/estados.json',
        '../json/municipios.json',
        '../csv/estados.csv',
        '../csv/municipios.csv',
    ]
    check_files(file_paths)

