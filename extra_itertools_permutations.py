# itertools.permutations()


#import library
from itertools import permutations

#receive parameters
s,n = input().split()

#do iterations
result = ((permutations(s, int(n))))

#create an array with all elements
aux = []
for i in result:
    aux.append(''.join(i[0:len(i)]))
    
#sort elements    
aux.sort()

#print each element
for j in aux:
    print(j)
