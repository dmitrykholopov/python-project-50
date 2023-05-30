import json


def get_ev(value):
    return json.JSONEncoder().encode(value)


def generate_diff(file1_path, file2_path):
    dict1 = json.load(open(file1_path))
    dict2 = json.load(open(file2_path))
    united_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = '}\n'

    for key in united_keys:

        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                part = f'    {key}: {get_ev(dict1[key])}\n'
                result += part
            else:
                part = f'  - {key}: {get_ev(dict1[key])}\n'
                result += part
                part = f'  + {key}: {get_ev(dict2[key])}\n'
                result += part

        if key in dict1 and key not in dict2:
            part = f'  - {key}: {get_ev(dict1[key])}\n'
            result += part

        if key in dict2 and key not in dict1:
            part = f'  + {key}: {get_ev(dict2[key])}\n'
            result += part

    result += '}'

    return result
