.PHONY: install test lint format clean setup-hooks setup

PROJECT_NAME = permutations
ENV_NAME = ${PROJECT_NAME}_env

# Automated code formatting.
fmt:
# Could not find a way to run loop that works on both Windows and Linux
	pre-commit run --all-files

install:
	conda env update --file environment.yml --prune --name ${ENV_NAME}

test:
	pytest tests/ --cov=permutations

setup-hooks:
	pre-commit install

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
