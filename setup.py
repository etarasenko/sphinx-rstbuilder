# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='sphinx-rstbuilder',
    version='0.1',
    description='Sphinx extension to output human readable reST files.',
    url='https://github.com/etarasenko/sphinx-rstbuilder',
    author='Eugene Tarasenko',
    author_email='eugene.tarasenko@gmail.com',
    license='BSD',
    platforms='any',
    packages=find_packages(),
    install_requires=[
        'sphinx>=1.0',
    ],
)
