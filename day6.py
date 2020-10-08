number = int(input())
if number < 1 or number > 10:
    print("Number of tests is out of the limits")
else:
    count = 0
    while count < number:
        count += 1
        string = input()
        if len(string) < 1 or len(string) > 10000:
            print("String out of the limits")
        else:
            print(string[0:len(string):2] + ' ' + string[1:len(string):2])
