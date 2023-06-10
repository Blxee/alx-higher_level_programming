#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

/**
 * print_python_list_info - print information about python list
 *
 * @p: the list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, len = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	i = 0;
	while (i < len)
	{
		PyObject *elem = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, elem->ob_type->tp_name);
		Py_DECREF(elem);
		i++;
	}
}
