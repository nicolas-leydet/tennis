.PHONY: clean clean-test clean-pyc help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-pyc clean-test ## remove all test, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove pytest and coverage artifacts
	rm -fr .cache/
	rm -f .coverage
	rm -fr htmlcov/

lint: ## check style with flake8
	flake8 knogget tests


coverage: ## check code coverage with pytest and display report
	pytest --cov knogget --cov-report=html
	$(BROWSER) htmlcov/index.html

notebook:
	jupyter notebook .sandbox/&

start-postgresql: ## run smarodds postgresql image
	docker run --name smartodds_db -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=smartoods -d postgres

stop-postgresql: ## stop smarodds postgresql image
	docker stop smartodds_db || true
	docker rm smartodds_db
