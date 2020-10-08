#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return n
    else:
        # if not, calculate recursively
        return n * factorial(n-1)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    if n < 2 or n > 12:
        print("Number out of the limits")
    else:
        result = factorial(n)

        fptr.write(str(result) + '\n')

        fptr.close()
