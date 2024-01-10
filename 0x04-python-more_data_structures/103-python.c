#include <Python.h>
#include <object.h>
#include <bytesobject.h>

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
	size = ((PyVarObject *)p)->ob_size;  // Directly accessing ob_size from PyVarObject

	int print_size = (size < 10) ? size : 10;

	string = bytes->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %d bytes:", print_size + 1);

	for (i = 0; i <= print_size && string[i] != '\0'; i++) {
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}
