#!/usr/bin/env python3

from gendiff.modules.cli_parser import get_cli_parametres
from gendiff.modules.gendiff import generate_diff


def main():
    file1, file2 = get_cli_parametres()
    generate_diff(file1, file2)
# TODO REMOVE this from HERE!!!


if __name__ == '__main__':
    main()
