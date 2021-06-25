# Optional Imports

![Test](https://github.com/kevinsawade/optional_imports/actions/workflows/test.yml/badge.svg)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kevinsawade/c8f263678e4e1f57994fa049a83a85ab/raw/test.json)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kevinsawade/optional_imports/blob/main/examples.ipynb)


Small package that shows how to handle optional imports in python.

# Try it out in Google Colab

https://colab.research.google.com/github/kevinsawade/optional_imports/blob/main/examples.ipynb

# Install

```bash
$ pip install optional_imports
```
or, if you are working with virtual environments.
```bash
$ pip install --user optional_requirements
```

# Single File Set Up

Wget the file https://raw.githubusercontent.com/kevinsawade/optional_imports/main/opt_imports/optional_imports.py and put it into your package.

```bash
$ wget https://raw.githubusercontent.com/kevinsawade/optional_imports/main/opt_imports/optional_imports.py
```

# Usage

Import optional packages as such:

```python
from optional_imports import _optional_import
pd = _optional_import('pandas')
plt = _optional_import('matplotlib', 'pyplot')
random_array = _optional_import('numpy', 'random.random')
nonexistent = _optional_import('nonexistent_package')
```

Import will be postoned and an error will be raised if the module is not installed.

```python
>>> try:
...     nonexistent.function()
... except ValueError as e:
...     print(e)
Install the `nonexistent_package` package to make use of this feature.
```
