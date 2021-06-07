import unittest

test_cases = ()

import doctest
from import_main_project import optional_imports_module
doc_tests = (doctest.DocTestSuite(optional_imports_module), )

def load_tests(loader, tests, patter):
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        filtered_tests = [t for t in tests if not t.id().endswith('.test_session')]
        suite.addTests(filtered_tests)
    suite.addTests(doc_tests)
    return suite
