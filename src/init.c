#include "libstd.c"
#include <stdio.h>
const char* const module_docstring = "A python extension implementing the std::algorithm header";

static PyMethodDef python_std_algorithm_methods[] = {
    {"all_of_impl", all_of_impl, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef python_std_algorithm_module = {
    PyModuleDef_HEAD_INIT,
    "libstd", /* name of module */
    module_docstring,
    -1,
    python_std_algorithm_methods};

PyMODINIT_FUNC
PyInit_libstd(void) {
    return PyModule_Create(&python_std_algorithm_module);
}