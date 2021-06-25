#!/bin/bash

python -c "from optional_imports import _optional_import ; print('successfully imported')"
python -c "from optional_imports import _optional_import ; test = _optional_import('nonexistent_package', user_install=True) ; test() ; print('successfully auto-installed')"
