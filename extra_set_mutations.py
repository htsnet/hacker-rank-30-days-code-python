# Set Mutations


a = int(input())
setOfA = set(map(int, input().split()))

numberSets = int(input())
for i in range(numberSets):
    actionAndNumber = input().split()
    secondList = set(map(int, input().split()))
    if actionAndNumber[0] == 'update':
        setOfA.update(secondList)
    elif actionAndNumber[0] == 'intersection_update':
        setOfA.intersection_update(secondList)
    elif actionAndNumber[0] == 'difference_update':
        setOfA.difference_update(secondList)
    elif actionAndNumber[0] == 'symmetric_difference_update':
        setOfA.symmetric_difference_update(secondList)        
    else:
        pass

print(sum(list(setOfA))) 
