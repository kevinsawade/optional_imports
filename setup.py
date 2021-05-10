from setuptools import setup
import os
import re

# read _version.py to have a single source file for version.
exec(open('encodermap/_version.py').read())

# setup
setup(name='package_with_optional_packages',
      version=__version__,
      description='Example Python Library with optional packages, that inform the user about missing dependencies.',
      author='Kevin Sawade',
      url="https://github.com/AG-Peter/encodermap",
      packages=['package_with_optional_packages'],
      install_requires=[
          'numpy',
          'matplotlib',
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
      ])