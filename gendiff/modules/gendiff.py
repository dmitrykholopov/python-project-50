import json


def get_ev(value: str) -> str:
    return json.JSONEncoder().encode(value)


def is_updated_or_unchanged(key: str, dict1: dict, dict2: dict) -> str:
    result = ''

    if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                part = f'    {key}: {get_ev(dict1[key])}\n'
                result += part
            else:
                part = f'  - {key}: {get_ev(dict1[key])}\n'
                result += part
                part = f'  + {key}: {get_ev(dict2[key])}\n'
                result += part

    return result


def is_removed(key: str, dict1: dict, dict2: dict) -> str:
    result = ''
    part = f'  - {key}: {get_ev(dict1[key])}\n'
    result += part

    return result


def is_added(key: str, dict1: dict, dict2: dict) -> str:
    result = ''
    part = f'  + {key}: {get_ev(dict2[key])}\n'
    result += part

    return result


def get_result_string(dict1: dict, dict2: dict, united_keys: set) -> str:
    result = '}\n'

    for key in united_keys:

        if key in dict1 and key in dict2:
            result += is_updated_or_unchanged(key, dict1, dict2)

        if key in dict1 and key not in dict2:
            result += is_removed(key, dict1, dict2)

        if key in dict2 and key not in dict1:
            result += is_added(key, dict1, dict2)

    result += '}'

    return result


def generate_diff(file1_path: str, file2_path: str) -> str:
    dict1 = json.load(open(file1_path))
    dict2 = json.load(open(file2_path))
    united_keys = sorted(set(dict1.keys()) | set(dict2.keys()))

    return get_result_string(dict1, dict2, united_keys)
