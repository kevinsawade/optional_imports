"""Optional imports of python packages.

ToDo:
    * Interactively installing missing packages
    * More Examples

Examples:
    >>> from opt_imports.optional_imports import _optional_import
    >>> np = _optional_import('numpy')
    >>> np.array([1, 2, 3])
    array([1, 2, 3])
    >>> nonexistent = _optional_import('nonexistent_package')
    >>> try:
    ...     nonexistent.function()
    ... except ValueError as e:
    ...     print(e)
    Install the `nonexistent_package` package to make use of this feature.
    >>> try:
    ...     _ = nonexistent.variable
    ... except ValueError as e:
    ...     print(e)
    Install the `nonexistent_package` package to make use of this feature.
    >>> numpy_random = _optional_import('numpy', 'random.random')
    >>> np.random.seed(1)
    >>> np.round(numpy_random((5, 5)) * 20, 0)
    array([[ 8., 14.,  0.,  6.,  3.],
           [ 2.,  4.,  7.,  8., 11.],
           [ 8., 14.,  4., 18.,  1.],
           [13.,  8., 11.,  3.,  4.],
           [16., 19.,  6., 14., 18.]])

"""

PACKAGE_VERSION_MAPPING = {'xarray': '>=0.17.0'}

def _optional_import(module: str, name: str = None):
    import importlib
    try:
        module = importlib.import_module(module)
        if name is None:
            return module
        if '.' in name:
            for i in name.split('.'):
                module = getattr(module, i)
            return module
        return getattr(module, name)
    except ImportError as e:
        try:
            version = PACKAGE_VERSION_MAPPING[module]
            msg = f"Install the `{module}` package with version `{version}` to make use of this feature."
        except KeyError:
            msg = f"Install the `{module}` package to make use of this feature."

        import_error = e

        class _failed_import:
            def __init__(self, *args, **kwargs):
                pass

            def __call__(self, *args, **kwargs):
                raise ValueError(msg) from import_error

            def __getattribute__(self, *args, **kwargs):
                raise ValueError(msg) from import_error

            def __getattr__(self, *args, **kwargs):
                raise ValueError(msg) from import_error

        return _failed_import()
