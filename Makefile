
install:
	poetry install 

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even  

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 BRAIN_GAMES
