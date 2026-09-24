/*
 * File: c_listener_util.c
 * Date: 24-Sep-2026  M. Yokochi
 *
 * Optional C accelerator for the four hottest pure-Python helpers of
 * wwpdb/utils/nmr/mr/ParserListenerUtil.py:
 *
 *   copyFactor(factor)            minimal copy of a factor dictionary
 *   copyPolySeq(polySeq)          minimal copy of a polymer sequence
 *   atomKey(atom, exclKeys=())    hashable canonical form of an atom dictionary
 *   factorKey(factor)             hashable canonical form of a factor dictionary
 *
 * Every function is a byte-for-byte behavioral twin of the Python body it
 * replaces, including the exact-type tests (`v.__class__ is list`,
 * `a.__class__ is dict`), the insertion order of the result, and the exception
 * raised for an argument of the wrong type. ParserListenerUtil keeps the Python
 * bodies and rebinds the names only when this extension imports, so the package
 * stays pure Python wherever the extension was not built (DAOTHER-10315).
 *
 * Built only when WWPDB_NMR_BUILD_C_ACCEL=1 is set (see setup.py and the
 * Dockerfile builder stage), exactly like the speedy-antlr-tool accelerators.
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#ifndef Py_IS_TYPE
#define Py_IS_TYPE(ob, type) (Py_TYPE(ob) == (type))
#endif

/* Py_NewRef is 3.10+; this file is expected to build back to 3.9. */
#if PY_VERSION_HEX < 0x030A0000
static inline PyObject *
_c_listener_util_NewRef(PyObject *obj)
{
    Py_INCREF(obj);
    return obj;
}
#define Py_NewRef(obj) _c_listener_util_NewRef((PyObject *)(obj))
#endif


/* ---------------------------------------------------------------------------
 * copyFactor()
 * ------------------------------------------------------------------------ */

/*
 * [dict(a) if a.__class__ is dict else a for a in v], for an exact list v.
 */
static PyObject *
copy_list_of_atoms(PyObject *v)
{
    Py_ssize_t size = PyList_GET_SIZE(v);
    PyObject *out = PyList_New(size);

    if (out == NULL) {
        return NULL;
    }

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *elem = PyList_GET_ITEM(v, i);  /* borrowed */
        PyObject *copied;

        if (Py_IS_TYPE(elem, &PyDict_Type)) {
            copied = PyDict_Copy(elem);
            if (copied == NULL) {
                Py_DECREF(out);
                return NULL;
            }
        }
        else {
            copied = Py_NewRef(elem);
        }

        PyList_SET_ITEM(out, i, copied);  /* steals */
    }

    return out;
}

/*
 * The one value transform of copyFactor():
 *   [dict(a) if a.__class__ is dict else a for a in v] if v.__class__ is list else v
 */
static PyObject *
copy_factor_value(PyObject *v)
{
    if (Py_IS_TYPE(v, &PyList_Type)) {
        return copy_list_of_atoms(v);
    }

    return Py_NewRef(v);
}

/*
 * Non-exact-dict argument. Going through .items() reproduces the Python
 * comprehension's behavior for mappings, and its AttributeError for anything
 * that is not one.
 */
static PyObject *
copy_factor_generic(PyObject *factor)
{
    PyObject *items = PyObject_CallMethod(factor, "items", NULL);

    if (items == NULL) {
        return NULL;
    }

    PyObject *fast = PySequence_Fast(items, "factor.items() is not iterable");

    Py_DECREF(items);

    if (fast == NULL) {
        return NULL;
    }

    PyObject *out = PyDict_New();

    if (out == NULL) {
        Py_DECREF(fast);
        return NULL;
    }

    Py_ssize_t size = PySequence_Fast_GET_SIZE(fast);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PySequence_Fast_GET_ITEM(fast, i);  /* borrowed */
        PyObject *k = PySequence_GetItem(item, 0);
        PyObject *v = NULL;
        PyObject *copied = NULL;
        int rc = -1;

        if (k != NULL) {
            v = PySequence_GetItem(item, 1);
        }

        if (v != NULL) {
            copied = copy_factor_value(v);
        }

        if (copied != NULL) {
            rc = PyDict_SetItem(out, k, copied);
        }

        Py_XDECREF(copied);
        Py_XDECREF(v);
        Py_XDECREF(k);

        if (rc < 0) {
            Py_DECREF(out);
            Py_DECREF(fast);
            return NULL;
        }
    }

    Py_DECREF(fast);

    return out;
}

PyDoc_STRVAR(copy_factor_doc,
             "copyFactor(factor, /)\n--\n\n"
             "Return a copy of a factor dictionary, equivalent to deepcopy() for factor contents.");

static PyObject *
c_copy_factor(PyObject *module, PyObject *factor)
{
    (void)module;

    if (!PyDict_CheckExact(factor)) {
        return copy_factor_generic(factor);
    }

    PyObject *out = PyDict_New();

    if (out == NULL) {
        return NULL;
    }

    Py_ssize_t pos = 0;
    PyObject *k, *v;

    while (PyDict_Next(factor, &pos, &k, &v)) {
        PyObject *copied = copy_factor_value(v);
        int rc;

        if (copied == NULL) {
            Py_DECREF(out);
            return NULL;
        }

        rc = PyDict_SetItem(out, k, copied);
        Py_DECREF(copied);

        if (rc < 0) {
            Py_DECREF(out);
            return NULL;
        }
    }

    return out;
}


/* ---------------------------------------------------------------------------
 * copyPolySeq()
 * ------------------------------------------------------------------------ */

/*
 * {k: (list(v) if v.__class__ is list else v) for k, v in ps.items()}
 */
static PyObject *
copy_poly_seq_item(PyObject *ps)
{
    if (!PyDict_CheckExact(ps)) {
        /* Mirrors the Python comprehension: .items() or AttributeError. */
        PyObject *items = PyObject_CallMethod(ps, "items", NULL);
        PyObject *out;

        if (items == NULL) {
            return NULL;
        }

        out = PyDict_New();

        if (out == NULL) {
            Py_DECREF(items);
            return NULL;
        }

        PyObject *fast = PySequence_Fast(items, "items() is not iterable");

        Py_DECREF(items);

        if (fast == NULL) {
            Py_DECREF(out);
            return NULL;
        }

        Py_ssize_t size = PySequence_Fast_GET_SIZE(fast);

        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *item = PySequence_Fast_GET_ITEM(fast, i);  /* borrowed */
            PyObject *k = PySequence_GetItem(item, 0);
            PyObject *v = NULL;
            PyObject *copied = NULL;
            int rc = -1;

            if (k != NULL) {
                v = PySequence_GetItem(item, 1);
            }

            if (v != NULL) {
                copied = Py_IS_TYPE(v, &PyList_Type)
                         ? PyList_GetSlice(v, 0, PyList_GET_SIZE(v))
                         : Py_NewRef(v);
            }

            if (copied != NULL) {
                rc = PyDict_SetItem(out, k, copied);
            }

            Py_XDECREF(copied);
            Py_XDECREF(v);
            Py_XDECREF(k);

            if (rc < 0) {
                Py_DECREF(out);
                Py_DECREF(fast);
                return NULL;
            }
        }

        Py_DECREF(fast);

        return out;
    }

    PyObject *out = PyDict_New();

    if (out == NULL) {
        return NULL;
    }

    Py_ssize_t pos = 0;
    PyObject *k, *v;

    while (PyDict_Next(ps, &pos, &k, &v)) {
        PyObject *copied = Py_IS_TYPE(v, &PyList_Type)
                           ? PyList_GetSlice(v, 0, PyList_GET_SIZE(v))
                           : Py_NewRef(v);
        int rc;

        if (copied == NULL) {
            Py_DECREF(out);
            return NULL;
        }

        rc = PyDict_SetItem(out, k, copied);
        Py_DECREF(copied);

        if (rc < 0) {
            Py_DECREF(out);
            return NULL;
        }
    }

    return out;
}

PyDoc_STRVAR(copy_poly_seq_doc,
             "copyPolySeq(polySeq, /)\n--\n\n"
             "Return a copy of a polymer sequence, equivalent to deepcopy() for its contents.");

static PyObject *
c_copy_poly_seq(PyObject *module, PyObject *polySeq)
{
    (void)module;

    PyObject *fast = PySequence_Fast(polySeq, "argument is not iterable");

    if (fast == NULL) {
        return NULL;
    }

    Py_ssize_t size = PySequence_Fast_GET_SIZE(fast);
    PyObject *out = PyList_New(size);

    if (out == NULL) {
        Py_DECREF(fast);
        return NULL;
    }

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *copied = copy_poly_seq_item(PySequence_Fast_GET_ITEM(fast, i));

        if (copied == NULL) {
            Py_DECREF(out);
            Py_DECREF(fast);
            return NULL;
        }

        PyList_SET_ITEM(out, i, copied);  /* steals */
    }

    Py_DECREF(fast);

    return out;
}


/* ---------------------------------------------------------------------------
 * atomKey()
 * ------------------------------------------------------------------------ */

PyDoc_STRVAR(atom_key_doc,
             "atomKey(atom, exclKeys=(), /)\n--\n\n"
             "Return a hashable canonical form of a given atom, ignoring the given keys.");

static PyObject *
c_atom_key(PyObject *module, PyObject *const *args, Py_ssize_t nargs)
{
    (void)module;

    if (nargs < 1 || nargs > 2) {
        PyErr_SetString(PyExc_TypeError, "atomKey() takes 1 or 2 positional arguments");
        return NULL;
    }

    PyObject *atom = args[0];
    PyObject *exclKeys = nargs == 2 ? args[1] : NULL;

    if (!PyDict_CheckExact(atom)) {
        /* Reach .items() the way the generator expression would. */
        PyObject *items = PyObject_CallMethod(atom, "items", NULL);
        PyObject *res;

        if (items == NULL) {
            return NULL;
        }

        res = PySequence_List(items);
        Py_DECREF(items);

        if (res == NULL) {
            return NULL;
        }

        /* Filter, sort, freeze. */
        if (exclKeys != NULL) {
            Py_ssize_t i = 0;

            while (i < PyList_GET_SIZE(res)) {
                PyObject *item = PyList_GET_ITEM(res, i);  /* borrowed */
                PyObject *k = PySequence_GetItem(item, 0);
                int contains;

                if (k == NULL) {
                    Py_DECREF(res);
                    return NULL;
                }

                contains = PySequence_Contains(exclKeys, k);
                Py_DECREF(k);

                if (contains < 0) {
                    Py_DECREF(res);
                    return NULL;
                }

                if (contains) {
                    if (PySequence_DelItem(res, i) < 0) {
                        Py_DECREF(res);
                        return NULL;
                    }
                }
                else {
                    i++;
                }
            }
        }

        if (PyList_Sort(res) < 0) {
            Py_DECREF(res);
            return NULL;
        }

        PyObject *tuple = PyList_AsTuple(res);

        Py_DECREF(res);

        return tuple;
    }

    PyObject *pairs = PyList_New(0);

    if (pairs == NULL) {
        return NULL;
    }

    Py_ssize_t pos = 0;
    PyObject *k, *v;

    while (PyDict_Next(atom, &pos, &k, &v)) {
        PyObject *pair;
        int rc;

        if (exclKeys != NULL) {
            int contains = PySequence_Contains(exclKeys, k);

            if (contains < 0) {
                Py_DECREF(pairs);
                return NULL;
            }

            if (contains) {
                continue;
            }
        }

        pair = PyTuple_Pack(2, k, v);

        if (pair == NULL) {
            Py_DECREF(pairs);
            return NULL;
        }

        rc = PyList_Append(pairs, pair);
        Py_DECREF(pair);

        if (rc < 0) {
            Py_DECREF(pairs);
            return NULL;
        }
    }

    /* list.sort() is what sorted() runs, so the ordering matches by construction. */
    if (PyList_Sort(pairs) < 0) {
        Py_DECREF(pairs);
        return NULL;
    }

    PyObject *out = PyList_AsTuple(pairs);

    Py_DECREF(pairs);

    return out;
}


/* ---------------------------------------------------------------------------
 * factorKey()
 * ------------------------------------------------------------------------ */

/*
 * tuple(tuple(a.items()) if a.__class__ is dict else a for a in v), for an
 * exact list v.
 */
static PyObject *
factor_key_list(PyObject *v)
{
    Py_ssize_t size = PyList_GET_SIZE(v);
    PyObject *out = PyTuple_New(size);

    if (out == NULL) {
        return NULL;
    }

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *elem = PyList_GET_ITEM(v, i);  /* borrowed */
        PyObject *frozen;

        if (Py_IS_TYPE(elem, &PyDict_Type)) {
            Py_ssize_t nitems = PyDict_GET_SIZE(elem);
            Py_ssize_t pos = 0, j = 0;
            PyObject *ak, *av;

            frozen = PyTuple_New(nitems);

            if (frozen == NULL) {
                Py_DECREF(out);
                return NULL;
            }

            while (PyDict_Next(elem, &pos, &ak, &av)) {
                PyObject *pair = PyTuple_Pack(2, ak, av);

                if (pair == NULL) {
                    Py_DECREF(frozen);
                    Py_DECREF(out);
                    return NULL;
                }

                PyTuple_SET_ITEM(frozen, j++, pair);  /* steals */
            }
        }
        else {
            frozen = Py_NewRef(elem);
        }

        PyTuple_SET_ITEM(out, i, frozen);  /* steals */
    }

    return out;
}

/*
 * Non-exact-dict argument: reach .items() the way the generator expression
 * would, so a Mapping works and anything else raises the same AttributeError.
 */
static PyObject *
factor_key_generic(PyObject *factor)
{
    PyObject *items = PyObject_CallMethod(factor, "items", NULL);

    if (items == NULL) {
        return NULL;
    }

    PyObject *fast = PySequence_Fast(items, "factor.items() is not iterable");

    Py_DECREF(items);

    if (fast == NULL) {
        return NULL;
    }

    Py_ssize_t size = PySequence_Fast_GET_SIZE(fast);
    PyObject *out = PyTuple_New(size);

    if (out == NULL) {
        Py_DECREF(fast);
        return NULL;
    }

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PySequence_Fast_GET_ITEM(fast, i);  /* borrowed */
        PyObject *k = PySequence_GetItem(item, 0);
        PyObject *v = NULL;
        PyObject *frozen = NULL;
        PyObject *pair = NULL;

        if (k != NULL) {
            v = PySequence_GetItem(item, 1);
        }

        if (v != NULL) {
            frozen = Py_IS_TYPE(v, &PyList_Type) ? factor_key_list(v) : Py_NewRef(v);
        }

        if (frozen != NULL) {
            pair = PyTuple_Pack(2, k, frozen);
        }

        Py_XDECREF(frozen);
        Py_XDECREF(v);
        Py_XDECREF(k);

        if (pair == NULL) {
            Py_DECREF(out);
            Py_DECREF(fast);
            return NULL;
        }

        PyTuple_SET_ITEM(out, i, pair);  /* steals */
    }

    Py_DECREF(fast);

    return out;
}

PyDoc_STRVAR(factor_key_doc,
             "factorKey(factor, /)\n--\n\n"
             "Return a hashable canonical form of a factor dictionary, for use as a cache key.");

static PyObject *
c_factor_key(PyObject *module, PyObject *factor)
{
    (void)module;

    if (!PyDict_CheckExact(factor)) {
        return factor_key_generic(factor);
    }

    Py_ssize_t size = PyDict_GET_SIZE(factor);
    PyObject *out = PyTuple_New(size);

    if (out == NULL) {
        return NULL;
    }

    Py_ssize_t pos = 0, i = 0;
    PyObject *k, *v;

    while (PyDict_Next(factor, &pos, &k, &v)) {
        PyObject *frozen = Py_IS_TYPE(v, &PyList_Type) ? factor_key_list(v) : Py_NewRef(v);
        PyObject *pair;

        if (frozen == NULL) {
            Py_DECREF(out);
            return NULL;
        }

        pair = PyTuple_Pack(2, k, frozen);
        Py_DECREF(frozen);

        if (pair == NULL) {
            Py_DECREF(out);
            return NULL;
        }

        PyTuple_SET_ITEM(out, i++, pair);  /* steals */
    }

    return out;
}


/* ---------------------------------------------------------------------------
 * Module definition
 * ------------------------------------------------------------------------ */

static PyMethodDef c_listener_util_methods[] = {
    {"copyFactor", (PyCFunction)c_copy_factor, METH_O, copy_factor_doc},
    {"copyPolySeq", (PyCFunction)c_copy_poly_seq, METH_O, copy_poly_seq_doc},
    {"atomKey", (PyCFunction)(void (*)(void))c_atom_key, METH_FASTCALL, atom_key_doc},
    {"factorKey", (PyCFunction)c_factor_key, METH_O, factor_key_doc},
    {NULL, NULL, 0, NULL}
};

PyDoc_STRVAR(c_listener_util_doc,
             "C accelerators for the hottest helpers of ParserListenerUtil (DAOTHER-10315).");

static struct PyModuleDef c_listener_util_module = {
    PyModuleDef_HEAD_INIT,
    "c_listener_util",
    c_listener_util_doc,
    -1,
    c_listener_util_methods,
    NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit_c_listener_util(void)
{
    return PyModule_Create(&c_listener_util_module);
}
