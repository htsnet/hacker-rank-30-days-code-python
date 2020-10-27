# Check Subset


qtd = int(input())
for i in range(qtd):
    noUseA = int(input())
    setA = set(list(map(int, input().split())))
    noUseB = int(input())
    setB = set(list(map(int, input().split())))
    print(setA.issubset(setB))
