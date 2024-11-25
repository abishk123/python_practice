# WAP TO CHECK THE GIVEN NUMBER IS ARMSTRONG NUMBER OR NOT
'''the sum of individual number with the power of no of digits in given number'''
'''
n=int(input('n:'))
dummy=n
sum=0
l=len(str(dummy))
while dummy>0:
    rem=dummy%10
    sum+=rem**l
    dummy//=10
if sum==n:
    print(n,' is an armstrong number')
else:
    print(n,' is not an armstrong number')
'''

#APPROACH-2
'''


'''
#WAP TO CHECK THE GIVEN NUMBER IS DISARIUM OR NOT
'''IF THE NUMBER IS EQUALS TO THE SUM OF ITS INDIVIDUAL DIGITS
TO THE POWER OF ITS POSITION
EG: 135 = 1**1 + 3**2 + 5**3'''
'''
n=int(input('n:'))
l=len(str(n))
dummy=n
sum=0 
while dummy>0:
    rem = dummy%10
    sum+=rem**l
    dummy//=10
    l-=1
if sum==n:
    print(n,' is a disarium number')
else:
    print(n,'is not a disarium number')
'''

n=int(input('n:'))
l=len(str(n)) #last index position
dummy=n
sum=0
while l>0:
    rem = dummy%10
    sum+=rem**l
    dummy//=10
    l-=1
if sum==n:
    print(n,' is a disarium number')
else:
    print(n,'is not a disarium number')



'''
n=int(input('n:'))
l = len(str(n))
summ=0
dummy=n
while dummy>0:

# WAP PROGRAM TO CHECK THE GIVEN NUMBER IS HARSHAD NUMBER OR NOT
#IF THE GIVEN NUMBER IS DIVISIBLE BY ITS SUM OF ITS DIGITS THEN THE NUMBER IS HARSHAD NUMBER'''

'''
n=int(input('n:'))
dummy=n
summ=0
while dummy>0:
    rem = dummy%10
    summ+=rem
    dummy//=10
if n%summ==0:
    print(n,' is harshad number')
else:
    print(n,' is not an harshad number')

'''