from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        # Import and show tutorial after installation
        try:
            from doglang.tutorial import show_tutorial
            show_tutorial()
        except ImportError:
            print("Could not display tutorial. You can view it later by running: python -m doglang.tutorial")

setup(
    name="doglang",
    version="0.1.0",
    packages=find_packages(),
    description="A dog-themed programming language interpreter",
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
    cmdclass={
        'install': PostInstallCommand,
    },
) 