#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - function that prints Python strings
 * @p: Python Object
 */
void print_python_string(PyObject *p)
{
	PyObject *str, *repr;
	Py_ssize_t i;

	(void)repr;
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t size = PyUnicode_GET_SIZE(p);
	Py_UNICODE *unicode = PyUnicode_AsUnicode(p);

	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ?
			"compact ascii" :
			"compact unicode object");
	printf("  length: %ld\n", size);
	printf("  value: ");
	for (i = 0; i < size; i++)
	{
		printf("%lc", unicode[i]);
	}
	printf("\n");
}

