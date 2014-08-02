#!/usr/bin/env python
""" Tests for the sum implementation. """

import pytest

SINE_ERROR_MARGIN = 0.0016


@pytest.fixture(scope='module')
def refsine(request):
    """ Import the math module. """
    m = __import__("math")
    return lambda x: m.sin(m.radians(x))


#@pytest.fixture(scope='module')
#def sine_error_margin():
    #return 0.0015  # The worst-case margin of our algorithm is 0.0016...


@pytest.fixture(scope='module', params=range(0, 360, 5))
def angle(request):
    return request.param


def test_sin_error_margin(module, refsine):
    """ Check that output values are within acceptable error margins. """
    for angle in range(0, 360):
        assert abs(refsine(angle) - module.sin(angle)) < SINE_ERROR_MARGIN


#def test_sin_error_margin(module, refsine, angle):
    #""" Check that output values are within acceptable error margins. """
    #assert abs(refsine(angle) - module.sin(angle)) < SINE_ERROR_MARGIN


def test_sin_negative_input(module, refsine):
    """ Check that the function handles negative angles. """
    angle = -1
    assert abs(refsine(angle) - module.sin(angle)) < SINE_ERROR_MARGIN
