# itertools.product()


# call the library
from itertools import product

# ask for the elements
elementsA = list(map(int, input().split()))
elementsB = list(map(int, input().split()))

# iterate
print(*product(elementsA, elementsB))
