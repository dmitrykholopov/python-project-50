#!/usr/bin/env python3

from gendiff.modules.cli_parser import get_cli_parametres
import json


def generate_diff(file1_path, file2_path):
    dict1 = json.load(open(file1_path))
    dict2 = json.load(open(file2_path))
    common_keys = sorted(tuple({**dict1, **dict2}.keys()))
    result = '{\n'
    for key in common_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                part = f'    {key}: {dict1[key]}\n'
                result += part
            else:
                part = f'  - {key}: {dict1[key]}\n'
                result += part
                part = f'  + {key}: {dict2[key]}\n'
                result += part
        if key in dict1 and key not in dict2:
            part = f'  - {key}: {dict1[key]}\n'
            result += part
        if key in dict2 and key not in dict1:
            part = f'  + {key}: {dict2[key]}\n'
            result += part
    result += '}'
    return result


def main():
    get_cli_parametres()


if __name__ == '__main__':
    main()
