# Exceptions - String to Integer

#!/bin/python3

import sys


S = input().strip()

try:
    val = int(S)
    print(val)
except:
    print("Bad String")
