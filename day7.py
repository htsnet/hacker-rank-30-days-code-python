#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    if n < 1 or n > 1000:
        print("Number out of the limits.")
    else:
        arr = list(map(int, input().rstrip().split()))
        for i in arr:
            if i < 1 or i > 10000:
                print(f"Value {i} out of the limits")
        
        arr.reverse()
        for i in arr:
            print(i, end=" ")
