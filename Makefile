#!/usr/bin/env python
install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

remove-dist:
	rm -r dist

package-force-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 brain_games

pip-upgrade:
	python3 -m pip install --upgrade pip
