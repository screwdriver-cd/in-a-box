#!/usr/bin/env python
"""
Package setup file for python module ouroath.python_project
"""
import os
import setuptools
import sys


def setuptools_version_supported():
    major, minor, patch = setuptools.__version__.split('.')
    if int(major) > 31:
        return True
    return False


if __name__ == '__main__':
    if not setuptools_version_supported():
        print('Setuptools version 32.0.0 or higher is needed to install this package')
        sys.exit(1)

    # We're being run from the command line so call setup with our arguments
    setuptools.setup()

