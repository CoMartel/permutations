.PHONY: install test lint format clean setup-hooks setup

install:
	pip install -e ".[dev]"

test:
	pytest tests/ --cov=permutations

lint:
	ruff check permutations/
	mypy permutations/

format:
	docformatter --in-place --recursive permutations/
	ruff format permutations/
	ruff check --fix permutations/

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

setup: install setup-hooks 