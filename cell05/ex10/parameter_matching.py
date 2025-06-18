#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print("What was the parameter?", end=' ')
    user_input = input()
    if user_input == args[0]:
        print("Good job!")
    else :
        print("Nope, sorry...")