from json import load as json_load

from gendiff.modules.cli_parser import get_cli_parametres


def load_files_data():
    file1_path, file2_path = get_cli_parametres()
    dict1 = json_load(open(file1_path))
    dict2 = json_load(open(file2_path))

    return dict1, dict2
