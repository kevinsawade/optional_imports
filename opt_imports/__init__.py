from ._version import __version__
from .sub_package_1 import __init__
from .sub_package_2 import __init__
import os
print(os.getcwd())
print(os.listdir(os.getcwd() + '/opt_imports/'))
from .sub_project import __init__
