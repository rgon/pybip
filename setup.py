# Copyright (c) 2018 Kannan Subramani <Kannan.Subramani@bmw.de>
# SPDX-License-Identifier: GPL-3.0
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="BIP",
    version="1.0.0",
    description="Bluetooth - Basic Imaging Profile",
    author="Kannan Subramani <Kannan.Subramani@bmw.de>",
    license="GPL-3.0",
    classifiers=[
        "Development Status :: 5 - In progress/Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.8"
    ],
    keywords="BIP",
    packages=find_packages(),
    zip_safe=False,
    dependency_links=["https://github.com/nikhilkumarsingh/PyOBEX3"],
    install_requires=[
        "cmd2",
        "python-dateutil",
        "pybluez",
        "pillow>=8.0",
        "pyobex>=0.26"],
    extra_require={
        "develop": [
            "generateDS==2.28b"
            # TODO: Not sure how to add this as development dependency (not a python repo)
            # dtd2xsd (https://github.com/reposit/dtd2xs)
        ]
    }
)
