from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rdb',

    version='0.1.0',
    description='Standalone copy of celery.contrib.rdb',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/davidszotten/rdb',

    # Choose your license
    license='BSD',

    py_modules=['rdb'],
    install_requires=['billiard'],

)
