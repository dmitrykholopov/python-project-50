import os
import pytest


from gendiff.modules import cli_parser


def test_help():
    exit_status = os.system('gendiff -h')

    assert exit_status == 0


def test_cli_without_arg():

    with pytest.raises(SystemExit) as pytest_error:
        cli_parser.get_cli_parametres()()

    assert pytest_error.type == SystemExit
    assert pytest_error.value.code == 2