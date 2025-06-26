from setuptools import setup, find_packages

setup(
    name="permutations",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "pytest>=6.0.0",
    ],
    extras_require={
        "dev": [
            "pre-commit>=3.5.0",
            "ruff>=0.2.0",
            "mypy>=1.7.0",
            "pytest-cov>=4.1.0",
            "docformatter>=1.7.5",
            "types-pyyaml>=6.0.12.12",
            "types-setuptools>=57.4.14",
            "types-python-dateutil>=2.8.19.14",
        ]
    },
    python_requires=">=3.8",
    author="Corelyo",
    description="A package for permutation analysis and optimization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
) 