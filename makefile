main:
	@poetry run python src/main.py

test-all:
	@poetry run python  -m unittest

test-helper:
	@poetry run python  -m unittest discover ./tests/helper/

test-plataform:
	@poetry run python  -m unittest discover ./tests/plataform/

test-report:
	@poetry run python  -m unittest discover ./tests/reports/

test-pypdf2:
	@poetry run python  -m unittest discover ./tests/reports/pypdf2/

test-pytesseract-default:
	@poetry run python  -m unittest discover ./tests/reports/pytesseract/

linter:
	@poetry run flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
