#!/usr/bin/env python
from setuptools import setup

requires=['pelican>=3.4.0']

setup(
    name="i18n_subsites",
    version="0.0.1",
    url='https://github.com/getpelican/pelican-plugins',
    description="A plugin to extend the translations functionality by creating internationalized sub-sites for the default site.",
    package_dir={'i18n_subsites': ''},
    packages=['i18n_subsites'],
    install_requires=requires,
)
