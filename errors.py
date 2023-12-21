#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than Permission

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
else: 
    print("Success!")
finally:
    print("Run this every time.")
    
try:
    print(names[2])
except:
    print("[Error]: Missing name in the list")
    sys.exit(1)
    
