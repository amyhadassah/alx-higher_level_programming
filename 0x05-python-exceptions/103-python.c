#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	printf("  first 10 bytes:");
	for (i = 0; i < size && i < 10; i++)
		printf(" %02x", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_list - Print information about Python lists
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
		else if (PyList_Check(item))
			print_python_list(item);
		else if (PyTuple_Check(item))
			print_python_tuple(item);
		else if (PyLong_Check(item))
			print_python_int(item);
		else
			printf("%s\n", Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_float - Print information about Python float objects
 * @p: Python object (float)
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

/**
 * print_python_int - Print information about Python integer objects
 * @p: Python object (integer)
 */
void print_python_int(PyObject *p)
{
	printf("[.] int object info\n");

	if (!PyLong_Check(p))
	{
		printf("  [ERROR] Invalid Int Object\n");
		return;
	}

	printf("  value: %ld\n", PyLong_AsLong(p));
}

/**
 * print_python_tuple - Print information about Python tuple objects
 * @p: Python object (tuple)
 */
void print_python_tuple(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python tuple info\n");

	if (!PyTuple_Check(p))
	{
		printf("  [ERROR] Invalid Tuple Object\n");
		return;
	}

	size = PyTuple_Size(p);

	printf("[*] Size of the Python Tuple = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyTuple_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
		else if (PyList_Check(item))
			print_python_list(item);
		else if (PyTuple_Check(item))
			print_python_tuple(item);
		else if (PyLong_Check(item))
			print_python_int(item);
		else
			printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
