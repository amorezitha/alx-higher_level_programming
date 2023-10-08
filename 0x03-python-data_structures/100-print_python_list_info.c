#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about a Python list
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int allocated;
	int i;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
