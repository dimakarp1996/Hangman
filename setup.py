#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="Hangman",
    version="0.0.0",
    author="Dmitry Karpov",
    author_email="dimakarp1996@yandex.ru",
    url="https://github.com/dimakarp1996/Hangman", 
    license="MIT",
    packages=[
        "Hangman"
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        #"pytest-pylint",
        "pytest-pycodestyle",
        #"pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        #"pylint",
        "pycodestyle",
        #"pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
