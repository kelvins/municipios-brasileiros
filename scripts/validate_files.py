# -*- encoding: utf-8 -*-
import os
import csv
import simplejson

DIR = os.path.dirname(__file__)


def check_dict(items):
    """Check if there is an invalid value."""
    for item in items:
        invalid_item = any([
            None in item.keys(),
            None in item.values(),
            '' in item.keys(),
            '' in item.values(),
        ])
        if invalid_item:
            raise KeyError('Invalid key or value')


if __name__ == '__main__':
    file_path = os.path.join(DIR, '../municipios_brasileiros.json')
    with open(file_path, 'r') as json_file:
        check_dict(simplejson.loads(json_file.read()))

    file_path = os.path.join(DIR, '../municipios_brasileiros.csv')
    with open(file_path, 'r') as csv_file:
        check_dict(csv.DictReader(csv_file))
