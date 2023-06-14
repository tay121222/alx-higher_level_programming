#define _XOPEN_SOURCE 700

#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function prints info about python list
 * @p: pointer to address of pyobject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}
