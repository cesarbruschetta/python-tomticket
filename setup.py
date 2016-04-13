#
# Copyright 2016 Cesar Augusto
#
#

import os
import re

from setuptools import find_packages
from setuptools import setup

with open(os.path.join('tomticket', '__init__.py')) as init:
    source = init.read()
    m = re.search("__version__ = '(\d+\.\d+(\.(\d+|[a-z]+))?)'", source, re.M)
    __version__ = m.groups()[0]

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="python-tomticket",
    version=__version__,
    description="Tomticket API wrapper",
    long_description=long_description,
    author="John Keyes",
    author_email="john@keyes.ie",
    license="MIT License",
    url="http://github.com/cesarbruschetta/python-tomticket",
    keywords='tomticket crm python',
    classifiers=[],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests", "inflection", "certifi", "six"],
    zip_safe=False
)
