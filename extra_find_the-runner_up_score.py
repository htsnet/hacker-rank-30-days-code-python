#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    if n < 2 or n > 10:
        print("Number of elements out of the limits")
    else:
        for i in arr:
            if i < -100 or i > 100:
                print("At least one of the elements is out of the limits")
            
        arrNoDuplicates = list(dict.fromkeys(arr))
        arrNoDuplicates.sort()
        print(arrNoDuplicates[-2])
