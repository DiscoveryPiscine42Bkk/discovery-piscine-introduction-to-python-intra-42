#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for word in args:
        print(f"{word}: {len(word)}")