#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2021/2/3 2:30 下午
# @File  : setup.py.py
# @Author: johnson
# @Contact : github: johnson7788
# @Desc  :

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google_trans_new",
    version="1.1.9",
    author="LuShan",
    author_email="xx",
    description="xx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xxx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)