from setuptools import setup, find_packages

# to read the libraries needed from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# to setup the package
# cmd: pip install -e .
setup(
    name='MLOPS-PROJECT-1',
    version="0.1",
    author='Saumyadeep',
    packages=find_packages(),
    install_requires=requirements,
)