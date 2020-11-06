#include "libstd.h"

static PyObject* all_of_impl(PyObject* self, PyObject* args) {
    PyObject* collection;
    PyObject* unary_predicate;

    // Parse args of type "OO" (two PyObjects) into collection and unary_predicate
    if (!PyArg_ParseTuple(args, "OO", &collection, &unary_predicate)) {
        return NULL;
    }
    collection = PySequence_Fast(collection, "parameter collection does not support iteration");
    
    if (!PyCallable_Check(unary_predicate)) {
        PyErr_SetString(PyExc_TypeError,"parameter unary_predicate must be a callable");
        return NULL;
    }

    Py_RETURN_FALSE;
}
