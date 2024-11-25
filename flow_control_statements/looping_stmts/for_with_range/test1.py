# 1  print sum of first n numbers
'''
sum = 0
n = int(input('n:'))
for i in range(n+1):
    sum += i
print(sum)
'''
# 2  WAP TO PRINT FACTORIAL OF GIVEN NUMBER
'''
n = int(input('n : ')) # taking integer input from user
factorial = 1 # assuming n = 0,so 0! = 1
for i in range(1,n+1):
    factorial *= i
print('n! = ',factorial)
'''
# 3  WAP TO PRINT GIVEN NUMBER IS PERFECT OR NOT
'''if the given no is equals to sum of the divisors of given no,then we call it as perfect no
6 is perfect no because sum of its divisors(1,2,3) is 6
'''
'''
sum = 0
n = int(input('n : '))

for i in range(1,n):
    if  n%i == 0:
        sum += i
if sum == n:
    print(n,'is perfect number')
else:
    print(n,'is not a perfect number')

    
sum = 0
n = int(input('n:'))
for i in range(1,n//2+1):
    if n%i==0:
        sum += i
if sum == n:
    print('perfect')
else:
    print('not a perfect number')

# 4  WAP TO PRINT EVEN NUMBERS IN A GIVEN RANGE
ll = int(input('starting range : '))
ul = int(input('ending range : '))
 # time complexity is more and efficiency is less
for i in range(ll,ul+1):
    if i%2==0:
        print(i)

if ll%2!=0:
    ll=ll+1
for n in range(ll,ul+1,2):
    print(n)
'''

