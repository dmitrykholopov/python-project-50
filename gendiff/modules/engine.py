from gendiff.modules.cli_parser import get_cli_parametres
from gendiff.modules.gendiff import generate_diff


def make_diff() -> callable:
    file1, file2 = get_cli_parametres()
    print(generate_diff(file1, file2))
