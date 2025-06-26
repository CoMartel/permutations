# Permutations

A Python package for efficient permutation analysis and optimization.

## Installation

```bash
pip install -e .
```

For development installation with additional tools:
```bash
pip install -e ".[dev]"
```

## Project Structure

```
permutations/
├── permutations/         # Main package
│   ├── core/            # Core functionality
│   ├── algorithms/      # Permutation algorithms
│   ├── optimization/    # Optimization methods
│   ├── utils/          # Utility functions
│   └── visualization/  # Visualization tools
├── tests/              # Test suite
├── examples/           # Example notebooks and scripts
├── docs/              # Documentation
└── scripts/           # Utility scripts
```

## Development

1. Clone the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Run tests: `pytest tests/`
4. Format code: `black .`
5. Run type checks: `mypy permutations/`

## License

MIT License 