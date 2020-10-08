#2D Arrays


#!/bin/python3

import math
import os
import random
import re
import sys

def checkCConstraints(arr):
    process = True
    for i in range(6):
        for j in range(6):
            if arr[i][j] < -10 or arr[i][j] > 10:
                process = False
                break
    return process

def sumValue(arr, i, j):
    a = arr[i][j]
    b = arr[i][j+1]
    c = arr[i][j+2]
    d = arr[i+1][j+1]
    e = arr[i+2][j]
    f = arr[i+2][j+1]
    g = arr[i+2][j+2]
    return a + b + c + d + e + f + g

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    #check constrains
    process = checkCConstraints(arr)
    if process:
        maxValue = -9 * 7 # lower number X number of elements
        for i in range(len(arr) - 2): #the maximum options in the line
            for j in range(len(arr) - 2): #the maximum options in the row
                result = sumValue(arr, i, j)
                if maxValue < result:
                    maxValue = result
        
        print(maxValue)

    else:
        print("At least one number is out of limits.")
