#!/usr/bin/env python
""" Install script for native extensions. """

from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as BuildExt

__version = (0, 1, 0)


class BuildInPlace(BuildExt, object):

    """ Simple class to build external modules in-place.

    Calling this function will cause shared object libraries to be built
    and copied to the source code tree. This is useful e.g. when testing.

    This is the equivalent of calling `setup.py build_ext --inplace'

    """

    def finalize_options(self):
        """ Set --inplace for the build_ext command. """
        super(BuildInPlace, self).finalize_options()
        self.inplace += 1


class PyTest(BuildInPlace):

    """ Use py.test to run tests.

    This is copied from
      `http://pytest.org/latest/goodpractises.html#integrating-with-distutils-python-setup-py-test'

    We need to create the test script using `py.test --genscript=runtests.py'

    """

    user_options = []

    test_script = 'runtests.py'

    def run(self):
        """ Build extensions and run py.test. """
        # Call build_ext --inplace
        super(PyTest, self).run()

        # Run tests in a subprocess.
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, self.test_script])
        raise SystemExit(errno)


setup(
    name='ext_test',
    version='.'.join(map(str, __version)),
    packages=['ext_test', ],
    ext_modules=[
        Extension('ext_test.cmath', ['cmath.c', ]),
        Extension('ext_test.pymath', ['pymath.c', 'cmath.c', ]), ],
    scripts=['bin/ext_test_timer.py', 'bin/ext_test_sin.py', ],
    requires=['cffi', ],
    cmdclass={'test': PyTest}, )
