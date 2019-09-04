#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from distutils.core import setup, Extension

from os import path
from setuptools import setup, find_packages

here=path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'Readme.md'), encoding='utf-8') as f:
    long_description=f.read()

setup(
    name='gantt',
    version='0.1',
    author='Stefan Schinkel',
    author_email='mail@dreeg.org',
    license ='license.txt',
    keywords="gantt, project management",
    platforms=[
        "Operating System :: OS Independent",
    ],
    classifiers=[
        "Development Status :: Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Scheduling",
    ],
    # packages=['gantt'],
    url='https://github.com/stefanSchinkel/gantt',
    description='Simple gantt charts in python.',
    long_description=long_description,
    install_requires=[
        "matplotlib==3.0.3",
        "numpy==1.16.3"
    ],
    setup_requires=[
        "matplotlib==3.0.3",
        "numpy==1.16.3"
    ],
    include_package_data=True,
)
