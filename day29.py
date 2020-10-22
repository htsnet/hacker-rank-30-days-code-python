# Bitwise AND


#!/bin/python3

import math
import os
import random
import re
import sys

def find_max_bitwise(n, k):
    # variable to save the maximum value
    max_bitwise = 0
    for i in range(1, n+1):
        for j in range(1, i):
            bitwise = i & j ## attention: operator & 
            if max_bitwise < bitwise < k:
                max_bitwise = bitwise
                #just to end when the maximum is the defined
                if max_bitwise == k + 1:
                    return max_bitwise
    
    return max_bitwise

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(find_max_bitwise(n, k))
