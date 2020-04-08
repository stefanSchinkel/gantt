#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup

cwd = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(cwd, "Readme.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gantt",
    version="1.0",
    author="Stefan Schinkel",
    author_email="mail@dreeg.org",
    license="License :: OSI Approved :: MIT License",
    keywords="gantt, project management",
    platforms=[
        "Operating System :: OS Independent",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Scheduling",
    ],
    # packages=["gantt"],
    url="https://github.com/stefanSchinkel/gantt",
    description="Simple gantt charts in python.",
    long_description=long_description,
    install_requires=[],
    setup_requires=[
        "matplotlib=3.0.3",
        "numpy>=1.16.3"
    ],
    include_package_data=True,
)
