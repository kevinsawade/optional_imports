# import xarray as xr
import numpy as np
from ..optional_imports import _optional_import
xr = _optional_import('xarray')

__all__ = ['get_xarray_version']

def get_xarray_version():
    return xr.__version__
