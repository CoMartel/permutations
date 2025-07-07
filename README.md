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
│   └── table_rotation_example.py  # Example usage of the table rotation solver
├── permutations/
│   ├── __init__.py
│   └── core/
│       ├── __init__.py
│       └── table_rotation.py      # Table rotation solver implementation
├── tests/
│   └── test_core.py               # Unit tests
```

## Usage Example

See the file `examples/table_rotation_example.py` for an example of how to use the table rotation solver.

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
