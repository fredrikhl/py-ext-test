#!/usr/bin/env python
""" Simple script to run and time a function calls from each implementation. """
from ext_test.helpers import mathtime

for code in ('math.fib(15)',
             'math.sum(4567)',
             'math.hyp(30000.0, 40000.0)',
             'math.sin(45)'):
    print "Running code: '%s'" % code

    for mod in ('refmath', 'pymath', 'ctmath', 'cffimath', ):
        time = mathtime(code, module='ext_test.%s' % mod)
        print "  time using 'ext_test.%s': %.5f sec" % (mod, time)
