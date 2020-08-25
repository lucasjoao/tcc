main:
	@poetry run python src/main.py

test:
	@poetry run python  -m unittest

linter:
	@poetry run flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
