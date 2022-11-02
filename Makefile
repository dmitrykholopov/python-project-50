# Makefile

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest

install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

package-install:
	python3 -m pip install --user /Users/dmitrykholopov/HEXLET/python-project-50/dist/hexlet_code-0.1.0-py3-none-any.whl

package-uninstall:
	python3 -m pip uninstall /Users/dmitrykholopov/HEXLET/python-project-50/dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 /Users/dmitrykholopov/HEXLET/python-project-50

gendiff:
	poetry run gendiff

.PHONY: install test lint selfcheck check build