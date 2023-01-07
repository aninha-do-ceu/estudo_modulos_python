from setuptools import setup, find_packages
from pathlib import PurePath
import os

root_path = PurePath(os.path.abspath(__file__)).parents[0]
requirements_path = root_path / 'requirements.txt'

with open(requirements_path, encoding = "utf8") as fp:
    install_requires = fp.read()

setup(
    name = 'Estudo_modulo',
    version = '0.1',
    packages = find_packages()
)