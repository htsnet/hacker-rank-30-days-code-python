# Nested Logic



from datetime import datetime, timedelta
inputDateReturned = input().split()
inputDateExpected = input().split()

dateReturned = datetime.strptime(inputDateReturned[0].zfill(2) +
                                 inputDateReturned[1].zfill(2) + 
                                 inputDateReturned[2].zfill(4), '%d%m%Y')  

dateExpected = datetime.strptime(inputDateExpected[0].zfill(2) + 
                                 inputDateExpected[1].zfill(2) + 
                                 inputDateExpected[2].zfill(4), '%d%m%Y')   

# to calculate dif months
def months(d1, d2):
    return d1.month - d2.month + 12*(d1.year - d2.year)

if dateReturned <= dateExpected:
    print(0)
elif inputDateReturned[2] != inputDateExpected[2]:    
    #different year
    print(10000)    
elif inputDateReturned[1] != inputDateExpected[1]:
    #same year, different month
    months = months(dateReturned, dateExpected)
    print(months * 500)
else:    
    #same month and year
    days = (dateReturned -  dateExpected).days
    print(days * 15)
