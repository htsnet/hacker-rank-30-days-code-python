#!/bin/python3

def decimal_to_binary(n, long_value):
    #print("entrando", long_value)
    if n <= 1:
        #print('saindo', long_value + str(n))
        return long_value + str(n)
    else:
        remainder = n % 2
        n = n // 2
        long_value = long_value + str(remainder)
        #print("long", long_value)
        return decimal_to_binary(n, long_value)

if __name__ == '__main__':
    n = int(input())
    if n < 1 or n > 10**6:
        print("Number out of the limits.")
    else:
        result = decimal_to_binary(n, "")
        #print("tratando", result)
        
        count = 0
        last_count = 0
        for i in result:
            if i == "1":
                count += 1
            else:
                if count > last_count:
                    last_count = count
                count = 0
                
        #print(count, last_count)        
        if count > last_count:
            last_count = count                
        print(last_count)
