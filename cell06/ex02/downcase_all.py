#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in  args:
        print(arg.lower())
