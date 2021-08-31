#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open("README.md").read()

setup(
    name="android-lint-to-junit-xml",
    version="0.1.1",
    description="Convert android-lint xml outputs to a jUnit valid xml tests result file",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Vlad Onishchenko",
    author_email="me@vladonishchenko.ru",
    url="https://github.com/STFBEE/android-lint-to-junit-xml",
    packages=["androidlinttojunitxml"],
    package_dir={"android-lint-to-junit-xml": "androidlinttojunitxml"},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "android-lint-to-junit-xml = androidlinttojunitxml.androidlinttojunitxml:main"
        ]
    },
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords=["android", "lint", "junit", "report", "gradle"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
