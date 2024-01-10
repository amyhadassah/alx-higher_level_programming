#include <Python.h>
#include <object.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p) {
	char *string;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);

	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++) {
		printf(" %02x", (unsigned char)string[i]);
	}
	if (size > 10) {
		printf(" ...");
	}
	printf("\n");
}
