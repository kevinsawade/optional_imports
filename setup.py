from setuptools import setup
import os
import re

# read _version.py to have a single source file for version.
exec(open('opt_imports/_version.py').read())

# setup
setup(name='opt_imports',
      version=__version__,
      description='Example Python Library with optional packages, that inform the user about missing dependencies.',
      author='Kevin Sawade',
      url="https://gitlab.inf.uni-konstanz.de/kevin.sawade/optional_packages",
      packages=['opt_imports'],
      install_requires=[],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
      ])