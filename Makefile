#!/usr/bin/env python
install:
	poetry install

brain-games:
	poetry run brain-games 

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 pip uninstall hexlet-code

remove dist:
	rm -r dist

package-force-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

make lint:
	poetry run flake8 brain_games

