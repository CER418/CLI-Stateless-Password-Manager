from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A simple stateless CLI password manager.'

setup(
    name='Stateless CLI password manager',
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'password manager', 'stateless', 'hash digest', 'hashlib', 'click']
)
