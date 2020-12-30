#!/bin/env python3
# noqa: D100

import setuptools  # type: ignore

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

__version__ = "2.1.0"

setuptools.setup(
    name="pyaoi",
    version=__version__,
    author="Jonas Muehlmann",
    author_email="jonasmuehlmann@protonmail.com",
    description="A collection of useful functions operating on iterables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JonasMuehlmann/pyaoi",
    py_modules=["pyaoi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
