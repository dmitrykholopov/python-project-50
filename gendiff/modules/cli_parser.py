import argparse


def get_cli_parametres():
    # Description for our script
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    # Positional arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    # Optional arguments, we can add DEFAULT value too or do it REQUARED
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        dest='FORMAT'
                        )
    file_names = parser.parse_args()
    return file_names.first_file, file_names.second_file