#/usr/bin/env python
""" Ctypes wrapper module for the shared object library `cmath.so'. """


import ctypes
from .helpers import get_caller_dir


_lib = ctypes.CDLL(get_caller_dir("cmath.so"))


# fib
_lib.fib.restype = ctypes.c_uint64
_lib.fib.argtypes = [ctypes.c_uint64, ]
fib = _lib.fib

# sum
_lib.sum.restype = ctypes.c_uint64
_lib.sum.argtypes = [ctypes.c_uint64, ]
sum = _lib.sum

# hyp
_lib.hyp.restype = ctypes.c_double
_lib.hyp.argtypes = [ctypes.c_double, ctypes.c_double, ]
hyp = _lib.hyp

# sin
_lib.sine.restype = ctypes.c_double
_lib.sine.argtypes = [ctypes.c_int, ]
sin = _lib.sine
