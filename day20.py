# Sorting


import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

totalSwaps = 0

def eachSwap():
    global a, n
    # Track number of elements swapped during a single array traversal
    numberOfSwaps = 0;
    for i in range(n):
        for j in range(n - 1):
            # Swap adjacent elements if they are in decreasing order
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps += 1
                #print(numberOfSwaps)
    return numberOfSwaps

doIt = True
while doIt:
    result = eachSwap()
    if result > 0:
        totalSwaps += result
    else:
        doIt = False


print("Array is sorted in {} swaps.".format(totalSwaps))
print("First Element:", a[0])    
print("Last Element:", a[-1]) 
