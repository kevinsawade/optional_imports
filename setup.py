from setuptools import setup
import os
import re

# read _version.py to have a single source file for version.
exec(open('optional_imports/_version.py').read())

# setup
setup(name='optional_imports',
      version=__version__,
      description='Example Python Library with optional packages, that inform the user about missing dependencies.',
      author='Kevin Sawade',
      url="https://github.com/kevinsawade/optional_imports",
      packages=['optional_imports'],
      install_requires=[],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
      ])