# Running Time and Complexity (prime or not)


import math

def isPrime(value):
    # less 0, 0 or 1 is not prime
    if value < 2:
        return False
    else:
        i = 2
        #define the limit as the square root of the number
        limit = math.sqrt(value)
        while i <= limit:
            if value % i == 0:
                return False
            i += 1
        return True

t = int(input())
for i in range(t):
    thisNumber = int(input())
    prime = isPrime(thisNumber)

    if prime:
        print("Prime")
    else:
        print("Not prime")
