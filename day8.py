# Enter your code here. Read input from STDIN. Print output to STDOUT

number = int(input())
if number < 0 or number > 10**5:
    print("Number out of the limits")
else:
    phone_list = dict()
    for i in range (1, number + 1):
        data = input()
        parts = data.split(" ")
        phone_list[parts[0]] = parts[1]

    continue_asking = True
    while continue_asking:
        try:
            friend = input()
            if friend in phone_list:
                print(friend + '=' + phone_list[friend])
            else:
                print("Not found")
        except:
            continue_asking = False
            break
