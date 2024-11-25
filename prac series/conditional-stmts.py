#1. Write a Python program to find those numbers which are divisible by 7 and
#   multiples of 5, between 1500 and 2700 (both included).
'''
nl=[]
ll=1500
ul=2700
for i in range(ll,ul+1):
    if i%7==0 and i%5==0:
        nl.append(str(i))
print(','.join(nl))

nl2=[]
while ll<=ul:
    if ll%5==0 and ll%7==0:
        nl2.append(str(ll))
    ll+=1
print(','.join(nl2))

'''
#2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius
'''
cf=input('input is in:')
deg=int(input('deg:'))
if cf=='f':
    c=((deg-32)*5)/9
    print(c)
else:
    f=((deg*9)+(32*5))/5
    print(f)
    '''

#3. Write a Python program to guess a number between 1 and 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the
#      guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''
import random
def guess():
    x=int(input('guess:'))
    if x==random.randint(1,9):
        print('well guessed!')
        return
    guess()
guess()
'''
'''
import random
while True:
    guess_num=int(input('guess a number b/w 1 to 9 untill u guess it correct:'))
    if random.randint(1,9)==guess_num:
        print('WELL GUESSED...!')
        break
'''

#4. Write a Python program to construct the following pattern, using a nested for loop.
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
'''
n=5
stars=1
for row in range(1,2*(n)):
    for st in range(1,stars+1):
        print('*',end=' ')
    if row<n:
        stars+=1
    else:
        stars-=1
    print()
        '''
#  5. Write a Python program that accepts a word from the user and reverses it.
'''
str=input('str:')
rev_str=''
for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]
print(rev_str)
    
'''
#6. Write a Python program to count the number of even and odd numbers in a series of numbers
'''Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
''''''
numbers=eval(input('numbers:'))
even=[]
c_e=0
odd=[]
c_o=0
for i in numbers:
    if i%2==0:
        even.append(str(i))
        c_e+=1
    else:
        odd.append(str(i))
        c_o+=1
print(f'there are {c_e} even numbers,that are {','.join(even)}')
print(f'there are {c_o} odd numbers,that are {','.join(odd)}')
'''
#7. Write a Python program that prints each item and its corresponding type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
'''
sl=eval(input('sample list: '))
for ele in sl:
    print(ele,type(ele))
print(sl,type(sl))
'''
#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5
'''
op=''
for i in range(0,6+1):
    if i==6 or i==3:
        continue
    op+=str(i)+' '
print(op)
'''
#9. Write a Python program to get the Fibonacci series between 0 and 50.
'''Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34'''
'''
a,b=0,1
while b<50:
    print(b)
    a,b=b,a+b
'''
#10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of
#  the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
'''Sample Output :
fizzbuzz
1
2
fizz
4
buzz'''
'''
i=0
while i<=50:
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
    i+=1
'''
#11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
'''Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]'''
'''
rows=int(input('rows:'))
cols=int(input('cols:'))
for i in range(rows):
    for j in range(cols):
        print(i*j,end=' ')
    print()
'''
# 12. WAP THAT ACCEPTS A SEQUENCE OF 

# 13. WAP THAT ACCEPTS A SEQ OF COMMA SEPARATED 4 DIGIT NUMBERS AS ITS INPUT.THE PROGRAM WILL 
#     PRINT THE NUMBERS THAT AR DIVISIBLE BY 5 IN COMMA SEPARATED SEQ.
'''
l=list(map(int,input("l:").split()))
el=[]
for i in l:
    if i%5==0:
        el.append(i)
print(el)
'''
# 14.  wap that accepts a string and calculate the number of digits and letters
'''
inp=input("input: ")
num_c=0
str_c=0
spa_c=0
spec_c=0
for ip in range(len(inp)):
    if inp[ip].isdigit():
        num_c+=1
    elif inp[ip].isalpha():
        str_c+=1
    elif inp[ip].isspace():
        spa_c+=1
    else:
        spec_c+=1
print(f'digits : {num_c}')
print(f'strings : {str_c}')
print(f'spaces : {spa_c}')
print(f'special chars : {spec_c}')
'''
# 15.  wap to check the validity of passwords input by users
"""1 letter b/w a-z and 1 letter b/w A-Z and 1-number b/w 0-9 and 1 letter in[$@#] 
and min length is 6 and max length is 16"""

def validatePw():
    sp=0
    str_c=0
    d_c=0
    ul="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ul_c=0
    ll='abcdefghijklmnopqrstuvwxyz'
    ll_c=0
    special_char='$@#'
    spec_c=0
    o_c=0
    pw=input("password: ")
    if len(pw)>6 and len(pw)<16:
        for ip in range(len(pw)):
            if pw[ip].isspace():
                sp+=1
            elif pw[ip] in ul:
                ul_c+=1
            elif pw[ip] in special_char:
                spec_c+=1
            elif pw[ip] in ll:
                ll_c+=1
            elif pw[ip].isdigit():
                d_c+=1
            else:
                o_c+=1
    else:
        print("invalid password")
    if o_c>0 or sp>0 or ul_c==0 or ll_c==0 or spec_c==0 or d_c==0:
        print("invalid password")
    else:
        print("valid password")

validatePw()

# 16. Write a Python program to find numbers between 100 and 400 (both included) where each 
# digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence

#31. Write a Python program to calculate a dog's age in dog years.
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

#32. Write a Python program to check whether an alphabet is a vowel or consonant.

# 33. Write a Python program to convert a month name to a number of days.

#34.34. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

35. Write a Python program that checks whether a string represents an integer or not.

36. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.

37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.

38. Write a Python program to display the astrological sign for a given date of birth.

39. Write a Python program to display the sign of the Chinese Zodiac for the given year in which you were born.

40. Write a Python program to find the median of three values

41. Write a Python program to get the next day of a given date.

42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

43. Write a Python program to create the multiplication table (from 1 to 10) of a number.


                


