#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n < 2 and n > 20:
        print("Number out of the limits.")
    else:
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)
