#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read().replace(".. :changelog:", "")

requirements = ["requests"]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name="activecampaign",
    version="0.2.0",
    description="ActiveCampaign API client",
    long_description=readme + "\n\n" + history,
    author="Ben Lopatin",
    author_email="ben@benlopatin.com",
    url="https://github.com/bennylope/activecampaign",
    packages=["activecampaign"],
    package_dir={"activecampaign": "activecampaign"},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords="activecampaign",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    tests_require=test_requirements,
)
