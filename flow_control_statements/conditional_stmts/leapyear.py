year = int(input('year : '))

if year%400==0 or (year%4 == 0 and year%100 != 0):   
    print('leap year')
else:
    print('not a leap year')




'''if year%100 != 0 or year%4==0 and year%400==0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')'''
    


'''if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')'''


    
'''if year % 100 !=0:
    if year % 4 == 0:
        print('leap year')
    else:
        print('not a leap year')
elif year % 100 == 0:
    if year % 400 == 0:
        print('leap year')
    else:
        print('not a leap year')'''
    
