from setuptools import find_packages, setup

setup(
    name="permutations",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    author="Corelyo",
    description="A package for permutation analysis and optimization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
