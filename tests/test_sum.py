#!/usr/bin/env python
""" Tests for the sum implementation. """

import pytest

# The `module' fixture is defined in conftest.py of this folder.


def test_lower_edge_case(module):
    """ Check that certain inputs match the known output. """
    assert module.sum(0) == 0
    assert module.sum(1) == 0
    assert module.sum(2) == 1
    assert module.sum(3) == 3


def test_expected_input(module):
    """ Check that certain inputs match the known output. """
    assert module.sum(957) == 457446
    assert module.sum(8341) == 34781970
    assert module.sum(9641286) == 46477193046255


@pytest.mark.skipif(True, reason="Might cause an infinite loop and halt tests")
def test_negative_input(module):
    module.sum(-1)
