# Check Strict Superset


setA =  set(list(map(int, input().split())))
number = int(input())
checking = True
for i in range(number):
    addicionalSet =  set(list(map(int, input().split())))
    if addicionalSet.issubset(setA) is False:
        checking = False

print(checking)
