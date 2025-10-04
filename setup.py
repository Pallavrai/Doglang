from setuptools import setup, find_packages
import os

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "A dog-themed programming language interpreter"

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
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "doglang=doglang.cli:main",
        ],
    },
)