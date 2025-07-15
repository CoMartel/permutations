.PHONY: install test lint format clean setup-hooks setup venv

PROJECT_NAME = permutations
ENV_NAME = ${PROJECT_NAME}_env
PYTHON = python
VENV = .venv
VENV_BIN = ${VENV}/Scripts

# Création et activation de l'environnement virtuel
venv:
	${PYTHON} -m venv ${VENV}

# Installation des dépendances
install: venv
	${VENV_BIN}/pip install -r requirements.txt

# Automated code formatting.
fmt:
	pre-commit run --all-files

test:
	pytest tests

setup-hooks:
	pre-commit install

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf ${VENV}
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
