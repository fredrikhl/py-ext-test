/**
 * This file contains the CPython wrappers for `cmath.*'.
 *
 * If compiled as a shared library (usually done with distutils or setuptools to
 * get the correct flags), it can be imported directly as a python module.
 */
#include <Python.h>
#include <stdint.h>
#include "pymath.h"
#include "cmath.h"

static PyObject * py_fib(PyObject * self, PyObject * args)
{
    uint64_t n;
    if (! PyArg_ParseTuple(args, "K", &n)) {
        return NULL;
    }
    return Py_BuildValue("K", fib(n));
}

static PyObject * py_sum(PyObject * self, PyObject * args)
{
    uint64_t max;
    if (! PyArg_ParseTuple(args, "K", &max)) {
        return NULL;
    }
    return Py_BuildValue("K", sum(max));
}

static PyObject * py_hyp(PyObject * self, PyObject * args)
{
    double a, b;
    if (! PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return Py_BuildValue("d", hyp(a, b));
}

static PyObject * py_sin(PyObject * self, PyObject * args)
{
    int angle;
    if (! PyArg_ParseTuple(args, "i", &angle)) {
        return NULL;
    }
    return Py_BuildValue("d", sine(angle));
}

static PyMethodDef module_functions[] = {
    { "fib", py_fib, METH_VARARGS, "Return fibonacci number `n'." },
    { "sum", py_sum, METH_VARARGS, "Return the sum of all natural numbers lower than `max'." },
    { "hyp", py_hyp, METH_VARARGS, "Return length of hypotenuse, using Pythagoras theorem." },
    { "sin", py_sin, METH_VARARGS, "Return approximation of sine of an angle (in degrees)." },
    { NULL },
};

PyMODINIT_FUNC initpymath(void)
{
    Py_InitModule3("pymath", module_functions, "C implementations to test CPython.");
}
