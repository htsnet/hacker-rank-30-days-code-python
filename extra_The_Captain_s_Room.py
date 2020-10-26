# The Captain's Room
 

k = int(input())
rooms = list(map(int, input().split()))

# create a set for unique room and another to multiple room
unique = set()
multiple = set()

for i in rooms:
    if i in unique:
        multiple.add(i)
    else:
        unique.add(i)

#print the difference (only one room will be printed)
print(list(unique.difference(multiple))[0])
