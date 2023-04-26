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

patch:
	rm -R dist/
	poetry install
	poetry version patch
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

