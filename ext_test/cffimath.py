#/usr/bin/env python
""" CFFI wrapper module for the shared object library `cmath.so'. """

from cffi import FFI
from .helpers import get_caller_dir


_ffi = FFI()
_ffi.cdef("""
    uint64_t fib(uint64_t n);
    uint64_t sum(uint64_t max);
    double hyp(double a, double b);
    double sine(int angle);
""")

_lib = _ffi.dlopen(get_caller_dir("cmath.so"))

fib = _lib.fib
sum = _lib.sum
hyp = _lib.hyp
sin = _lib.sine
