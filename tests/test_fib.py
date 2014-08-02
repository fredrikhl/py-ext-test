#!/usr/bin/env python
""" Tests for the simple fibonacci implementation. """

import pytest

# The `module' fixture is defined in conftest.py of this folder.


def test_lower_edge_case(module):
    """ Check that certain inputs match the known output. """
    assert module.fib(0) == 0
    assert module.fib(1) == 1
    assert module.fib(2) == 1
    assert module.fib(3) == 2


def test_expected_output(module):
    """ Check that certain inputs match the known output. """
    assert module.fib(5) == 5
    assert module.fib(15) == 610
    assert module.fib(25) == 75025


@pytest.mark.skipif(True, reason="Might cause segfault and abort testing")
def test_negative_input(module):
    module.fib(-1)
