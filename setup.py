from setuptools import setup, find_packages
from setuptools.command.install import install
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="doglang",
    version="1.0.0-alpha",
    packages=find_packages(),
    description="A dog-themed programming language interpreter",
    long_description=long_description,  
    long_description_content_type="text/markdown",
    author="Pallav Rai",
    author_email="pallavrai8953@gmail.com",
    url="https://github.com/Pallavrai/doglang",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "doglang=doglang.cli:main",
        ],
    },
   
) 