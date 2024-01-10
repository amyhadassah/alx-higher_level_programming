#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p) {
	long size;
	PyListObject *list;
	PyObject *item;
	const char *type_name;
	int i;

	printf("[*] Python list info\n");

	if (!PyList_Check(p)) {
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++) {
		item = list->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %d: %s\n", i, type_name);
	}
}

void print_python_bytes(PyObject *p) {
	PyBytesObject *bytes;
	char *string;
	long size;
	int i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	string = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes:", (size < 10) ? size + 1 : 10);

	for (i = 0; i < ((size < 10) ? size + 1 : 10); i++) {
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}
