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
│   └── table_rotation_example.py  # Example usage of the table rotation solvers
├── permutations/
│   ├── __init__.py
│   └── core/
│       ├── __init__.py
│       ├── table_rotation.py      # Table rotation solver (constraint-based)
│       └── score_rotation.py      # Table rotation solver (score-based)
├── tests/
│   └── test_core.py               # Unit tests
```

## Table Rotation Solvers

- `table_rotation.py`: Generates table rotations using constraint satisfaction (forbidden pairs, etc).
- `score_rotation.py`: Generates table rotations using a scoring system to maximize gender diversity and minimize repeated pairings.

## Usage Example

See the file `examples/table_rotation_example.py` for an example of how to use the table rotation solvers.

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
