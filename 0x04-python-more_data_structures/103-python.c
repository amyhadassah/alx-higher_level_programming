#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p) {

	if (p == NULL) {
		printf("[ERROR] Invalid List Object\n");
		return; 
	}

	PyListObject *list = (PyListObject*)p;

	long size = list->ob_base.ob_size;

	printf("[*] Python list info\n");  
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (int i = 0; i < size; i++) {
		PyObject *item = list->ob_item[i];
		const char *type_name = item->ob_type->tp_name;
		printf("Element %d: %s\n", i, type_name);
	}
}

void print_python_bytes(PyObject *p) {

	if (p == NULL || !PyBytes_Check(p)) {
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytesObject *bytes = (PyBytesObject*)p;

	char *string = bytes->ob_sval; 
	long size = bytes->ob_base.ob_size;

	printf("[.] bytes object info\n");
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", string);  

	printf(" first 10 bytes:");
	for (int i = 0; i < 10; i++) {
		printf(" %02x", (unsigned char)string[i]); 
	}

	printf("\n");
}
