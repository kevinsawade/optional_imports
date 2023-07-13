# Change Log

DateFormat: yyyy-mm-dd
SemanticVersioning.

[1.0.0] - 2021-15-10 Relase

Release. Class inheritance did not work in that version.
Using statements like `from package.subpackage.subpackage.subpackage._hidden import _hiddenClass` did not work.
This was because only the getattr() method was used, but some objetcs are not accessible that way.
That's what the from X.Y.Z import Class syntax was for.

[1.0.1] - 2021-06-25 - Installation on-the-fly and Class inhertiance.

All goals seemed to be fulfilled in this version.

Added:
    - OOP with class inhertiance
    - Docstring for function
    - Two more arguments (`user_install` prompts the user for install, `auto_install` automatically installs missing packages).

Changed:
    - Docstring now part of `_optional_import` function.

[1.0.2] - 2021-06-25 - Increased version number to check github to PyPI workflow

[1.0.3] - 2023-06-13

Fixed issue with relative imports. Version 1.0.2 could not do `Client = optional_import("dask", "distributed.Client")`. This is now possible.
