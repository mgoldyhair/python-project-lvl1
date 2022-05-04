#!/usr/bin/env python
install:
	poetry install

brain-games:
	poetry run brain-games
	poetry run welcome-user

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

