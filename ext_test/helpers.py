#!/usr/bin/env python
""" Some helper functions. """


def get_caller_dir(add_filename=None):
    """ Get the directory of the module where this function was called.

    Optionally append a filename to the returned path.

    This is used to look up the path of other files that should exist alongside
    the code files, e.g. shared libraries. The installer puts shared libraries
    in site-packages (as if they were modules). If we're using some FFI to load
    and wrap these libraries, we'll need to find their absolute location.

    :type add_filename: str, None
    :param add_filename str: If not `None', append the filename to the returned
                             path.

    :rtype: str, None
    :return: Returns the path to the module directory as a string.
             Returns `None' if the module is not from a file. This typically
             happens if the module is stdin or an interactive session.

    """
    import os
    import inspect

    try:
        (frame, filename, line_number, function_name, lines, index) = (
            inspect.getouterframes(
                inspect.currentframe())[1])  # 0 is _this_ frame, 1 is the
                                             # caller, 2 is the callers caller.
    except IndexError:
        return None
        # Function was not called?

    if not os.path.exists(filename):
        return None
        # Probably '<stdin>'

    dirname = os.path.dirname(os.path.abspath(filename))
    if add_filename:
        return os.path.join(dirname, add_filename)
    return dirname


def get_self_dir(filename=None):
    """ Get the directory name of this file.

    Optionally append a filename to the path returned.

    :filename str: If given, join filename to the returned path.

    :returns str: The absolute path to this module.

    """
    return get_caller_dir(filename)


def mathtime(code, module="ext_test.pymath"):
    """ Time some executable code.

    Using the `timeit' module, this function runs a short piece of code, and
    reports the average runtime of 1000 iterations, best of 7 test runs.

    This is used to measure the efficiency of our `ext_test' implementation
    modules.

    :param code str: A piece of code to measure the runtime of.
    :param module str: A module to import during setup. The module is available
                       in the `code' under the name `math'.

    :returns float: The best of 7 test runs, measuring the average runtime of
                    1000 iterations (in seconds).

    """
    import timeit
    iterations = 1000  # Average of n iterations
    bestof = 7            # Do this n times, and report the best result.
    setup = "import %s as math" % module
    return min(timeit.Timer(code, setup=setup).repeat(bestof, iterations))
