#!/usr/bin/env python
""" Simple script to compare sine result from different implementations. """

from math import sin, radians

implementations = ('refmath', 'pymath', )
angles = (1, 5, 15, 30, 45, 90, 180, 210, 270, 359, )

funcs = {'math': lambda x: sin(radians(x)), }
for mod in implementations:
    funcs[mod] = getattr(
        __import__("ext_test.%s" % mod, fromlist=['ext_test', ]), 'sin')

for angle in angles:
    print "Angle %d deg" % angle
    for mod in funcs:
        res = funcs[mod](angle)
        print "  %s.sin(%d) = %.5f" % (mod, angle, res)
