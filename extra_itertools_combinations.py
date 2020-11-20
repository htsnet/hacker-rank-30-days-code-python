# itertools.combinations()

#import library
from itertools import combinations

#receive parameters
s,k = input().split()

#combine and print
for i in range(1, int(k)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))
