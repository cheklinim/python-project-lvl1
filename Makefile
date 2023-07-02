install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

patch:
	rm -R dist/
	poetry install
	poetry version patch
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

minor:
	rm -R dist/
	poetry install
	poetry version minor
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

major:
	rm -R dist/
	poetry install
	poetry version major
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

