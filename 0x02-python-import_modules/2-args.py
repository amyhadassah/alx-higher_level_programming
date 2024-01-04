#!/usr/bin/python3
import sys

n = len(sys.argv) - 1
print(f"{n} argument{'s' if n != 1 else ''}{'.' if n == 0 else ':'}")
for i, arg in enumerate(sys.argv[1:], 1):
    print(f"{i}: {arg}")
