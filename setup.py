#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import easyaerospike

setup(
    name='easyaerospike',
    version=easyaerospike.__version__,
    description='Work easier with Aerospike in Python',
    url='https://github.com/catenae/easyaerospike',
    author='Rodrigo Martínez Castaño',
    author_email='rodrigo@martinez.gal',
    license='GNU General Public License v3 (GPLv3)',
    packages=['easyaerospike'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['aerospike==3.9.0'])  # Dependencies
