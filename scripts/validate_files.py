# -*- encoding: utf-8 -*-
import os
import csv
import logging
import json

DIR = os.path.dirname(__file__)

# Cria os parametros do logger
logger = logging.getLogger('validate_files')
logger.setLevel(logging.INFO)

f_handler = logging.FileHandler(os.path.join(DIR, '../Validation.log'), encoding='utf-8')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

f_handler.setFormatter(f_format)
logger.addHandler(f_handler)


def check_dict(items):
    """Verifica se há valores inválidos nos dicts.

    Args:
        items (List[Dict]): Dicts a serem verificados

    Raises:
        KeyError: Se existir algum valor inválido no dict.
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
            logger.error(f'Dados inválidos em {item}')
            raise KeyError('Dados inválidos nesse item:', item)


def check_files(file_paths):
    """Verifica todos os arquivos da lista de caminhos de arquivo.

    Args:
        file_paths (List[str]): Lista com caminho para os arquivos.
    """
    for file_path in file_paths:
        logger.info(f'Verificando o arquivo {file_path}')
        with open(os.path.join(DIR, file_path), encoding='utf-8-sig', mode='r') as f:
            if file_path.endswith('.json'):
                check_dict(json.loads(f.read()))
            elif file_path.endswith('.csv'):
                check_dict(csv.DictReader(f))
            logger.info(f"Tudo certo com o arquivo {file_path}")


if __name__ == '__main__':
    file_paths = [
        '../json/estados.json',
        '../json/municipios.json',
        '../csv/estados.csv',
        '../csv/municipios.csv',
    ]
    check_files(file_paths)
