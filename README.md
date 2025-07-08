# Permutations

Permutations is a Python project for generating table rotations with constraints, for example to organize groups of students who should not be seated together repeatedly.

## Project Structure

```
Permutations/
├── environment.yml                # Environment dependencies (conda)
├── Makefile                       # Build and test commands
├── README.md                      # This file
├── ruff.toml                      # Ruff linter configuration
├── setup.py                       # Package installation script
├── examples/
│   └── score_rotation_example.py  # Example usage of the score rotation solver
├── permutations/
│   ├── __init__.py
│   └── core/
│       ├── __init__.py
│       └── score_rotation.py      # Table rotation solver (score-based)
├── tests/
│   └── test_score_rotation.py     # Unit tests for score rotation
```

## Table Rotation Solver

- `score_rotation.py`: Generates table rotations using a scoring system to maximize gender diversity and minimize repeated pairings.

## Usage Example

See the file `examples/score_rotation_example.py` for an example of how to use the score rotation solver.

## Installation

1. Clone the repository
2. Install dependencies:
   `make install`

## Tests

Run the tests with:
```
make test
```

## Linting

Check code quality with Ruff:
```
make fmt
```
