#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_bytes - prints info about a python bytes object
 *
 * @p: the python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *obj = (PyBytesObject *)p;
	PyObject *str_obj = PyObject_Str(p);
	const char *str = PyUnicode_AsUTF8(str_obj);
	long len = PyBytes_Size(p);
	int i;

	printf("[.] bytes object info\n");
	printf("\tsize: %ld\n", obj->ob_base.ob_size);
	printf("\ttrying string: %s\n", str);
	printf("\tfirst 6 bytes:");
	for (i = 0; i < len; i++)
		printf(" %2hhx", obj->ob_sval[i]);
	printf("\n");
	Py_DECREF(str_obj);
}

/**
 * print_python_list - prints info about a python list
 *
 * @p: the python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, len;

	if (p == NULL)
		return;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	i = 0;
	while (i < len)
	{
		PyObject *elem = PyList_GET_ITEM(p, i);

		printf("Element %ld: %s\n", i, elem->ob_type->tp_name);
		Py_DECREF(elem);
		i++;
	}
}
