#!/usr/bin/env python
""" Common code for all tests in the `tests' package. """

import pytest


@pytest.fixture(scope='module', params=['pymath',
                                        'ctmath',
                                        'cffimath', ])
def module(request):
    """ Fixture to choose an implementation module to test. """
    return __import__("ext_test.%s" % request.param, fromlist=['ext_test', ])
