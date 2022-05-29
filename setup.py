#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from drf_impersonate/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    if version_match := re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    ):
        return version_match[1]
    raise RuntimeError("Unable to find version string.")


version = get_version("drf_impersonate", "__init__.py")


if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
# history = open("CHANGELOG.rst").read().replace(".. :changelog:", "")
# requirements = open("requirements.txt").readlines()

setup(
    name="drf-impersonate",
    version=version,
    description="""Django app to allow superusers to "impersonate" other non-superuser accounts.""",
    long_description=readme,
    author="Sumit Singh",
    author_email="sumit.singh4613@gmail.com",
    url="https://github.com/101loop/drf-impersonate",
    packages=[
        "drf_impersonate",
    ],
    include_package_data=True,
    install_requires=[
        "django>=3.2,<5.0",
        "djangorestframework>=3.12.0,<4.0",
    ],
    license="MIT",
    zip_safe=False,
    keywords="drf-impersonate",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
