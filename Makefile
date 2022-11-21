install:
	poetry install
gendiff:
	poetry run gendiff
build: check
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
lint:
	poetry run flake8 gendiff
selfcheck:
	poetry check

check: selfcheck test lint

