#include <Python.h>

void print_python_list(PyObject *p) {

	if(!PyList_Check(p)) { 
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	long int size = PyList_Size(p);

	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	for(int i = 0; i < size; i++) {
		PyObject *item = list->ob_item[i];
		const char *type = item->ob_type->tp_name;  
		printf("Element %i: %s\n", i, type);
	}
}


void print_python_bytes(PyObject *p) {

	char *str;
	long int size;

	if(!PyBytes_Check(p) || !PyBytes_AsStringAndSize(p, &str, &size)) {
		printf("[ERROR] Invalid Bytes Object\n"); 
		return;
	}

	printf("[.] bytes object info\n");

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes:");
	for(int i = 0; i < size && i < 10; i++) {
		printf(" %02hhx", str[i]);  
	}

	printf("\n");

}
