#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission

try:
    names = open("names.txt").readlines()
    1/0 # Se fosse 1/0 seria um ZeroDivisionError
    print(names.append) # Se não tivesse esse atributo seria um AttributeError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"{str(e)}.")
    sys.exit(1)
try:
    print(names[2])
except:
    print("[Error]: Missing name in the list")
    sys.exit(1)
    
