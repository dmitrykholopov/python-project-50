import json


def get_ev(value: str) -> str:
    return json.JSONEncoder().encode(value)


def is_updated_or_unchanged(key: str, dict1: dict, dict2: dict) -> str:
    if key in dict1 and key in dict2:
        if dict1[key] == dict2[key]:
            return f'    {key}: {get_ev(dict1[key])}\n'

        else:
            part1 = f'  - {key}: {get_ev(dict1[key])}\n'
            part2 = f'  + {key}: {get_ev(dict2[key])}\n'

            return f'{part1}{part2}'


def is_removed(key: str, dict1: dict, dict2: dict) -> str:
    return f'  - {key}: {get_ev(dict1[key])}\n'


def is_added(key: str, dict1: dict, dict2: dict) -> str:
    return f'  + {key}: {get_ev(dict2[key])}\n'


def get_part_of_result(key: str, dict1: dict, dict2: dict) -> str:

    if key in dict1 and key in dict2:
        return is_updated_or_unchanged(key, dict1, dict2)

    if key in dict1 and key not in dict2:
        return is_removed(key, dict1, dict2)

    if key in dict2 and key not in dict1:
        return is_added(key, dict1, dict2)


def get_result_string(
        dict1: dict, dict2: dict, all_keys: set, result=None) -> str:
    result = result or []
    result.append('}\n')
    structured_res = [
        get_part_of_result(key, dict1, dict2)
        for key in all_keys
    ]
    result.extend(structured_res)
    result.append('}')

    return ''.join(result)


def generate_diff(file1_path: str, file2_path: str) -> str:
    dict1 = json.load(open(file1_path))
    dict2 = json.load(open(file2_path))
    united_keys = sorted(set(dict1.keys()) | set(dict2.keys()))

    return get_result_string(dict1, dict2, united_keys)
