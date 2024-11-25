#1. Write a Python program to calculate the sum of a list of numbers using recursion.[nested list]
'''
def sum(list):
    summ=0
    for i in list:
        if type(i)==int:
            summ+=i
        else:
            summ+=sum(i)
    return summ
print(sum([22,23,[22,[11],23],23]))
'''
#2. FLAT LIST
'''
def sum_list(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0]+sum_list(l[1:])
print(sum_list([1,2,3,4,5,6]))
'''
#3. Write a Python program to convert an integer to a string in any base using recursion .
'''
def convert_toString(number,base):
    str='0123456789ABCDEF'
    STR=''
    if number%10 in str

# Define a function named to_string that converts a number 'n' to a string representation
# in a given 'base' using a character set "0123456789ABCDEF"
def to_string(n, base):
    # Define a character set for the conversion in hexadecimal format
    conver_tString = "0123456789ABCDEF"
    
    # Check if the number 'n' is less than the specified base
    if n <base:
        # If 'n' is less than the base, return the corresponding character from the character set
        return conver_tString[n]
    else:
        # If 'n' is greater than or equal to the base, recursively call the to_string function
        # to convert the quotient (n // base) to a string and concatenate it with the remainder
        # (n % base) represented in the character set
        return to_string(n // base, base) + conver_tString[n % base]

# Print the result of calling the to_string function with the input values 2835 and 16
print(to_string(17, 16))
'''
#4. Write a Python program to get the factorial of a non-negative integer using recursion.
'''
def facto(n):
    if n<=0:
        return 1
    else:
        return n*facto(n-1)
print(facto(10))
'''
#5. Write a Python program to solve the Fibonacci sequence using recursion.
'''
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(10))
print(l)

n=10
a,b=0,1
print(a,b)
for i in range(n-2):
    a,b=b,a+b
    print(b)
'''
#6. Write a Python program to get the sum of a non-negative integer using recursion.
'''Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9'''
'''
def sum(n):
    if n==0:
        return 0
    else:
        return n%10 + sum(n//10)
print(sum(45))
'''
#7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
'''Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''
'''
def sum(n):
    if n<=0:
        return 0
    else:
        return n+sum(n-2)
print(sum(10))
'''
#8. Write a Python program to calculate the sum of harmonic series upto n terms.
'''Note: The harmonic sum is the sum of reciprocals of the positive integers.
ex: 1/1 + 1/2 + 1/3 +....'''
'''
def harmo_Sum(n):
    if n==1:
        return 1
    else:
        return  1/n + harmo_Sum(n-1)
print(harmo_Sum(3))
'''
#Write a Python program to calculate the geometric sum up to 'n' terms.
'''
def geometricSum(n):
    if n==0:
        return 1
    else:
        return 1/(pow(2,n))+geometricSum(n-1)
print(geometricSum(52))
print(geometricSum(7))
print(geometricSum(4))
'''
#10. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
'''Test Data :(power(3,4) -> 81'''
'''
def pov(b,p):
    if p==1:
        return b
    else:
        return b*pov(b,p-1)
print(pov(2,4))
'''
#11. Write a Python program to find the greatest common divisor (GCD) of two integers using recursion.
def hcf_gcd(a,b):
    if min(a,b)==0:
        return max(a,b)
    elif min(a,b)==1:
        return 1
    else:
        return hcf_gcd(min(a,b,), max(a,b,)%min(a,b,))
op=hcf_gcd(99,33)
print(op)







'''
def gcd(a,b):
    for i in range(b,a-1,-1):
        if a%i==0 and b%i==0:
            return i
print(gcd(10,40))'''





#power value
'''
def power(b,p):
    if p==0:
        return 1
    return b*power(b,p-1)
val=power(3,4)
print(val)
'''
'''
def harmonicseries(n):
    if n==0:
        return 0
    return 1/n + harmonicseries(n-1)

va=harmonicseries(3)
print(va)
'''
# 1  WAP TO PRINT SUM OF EACH AND EVERY ELEMENTS OF NESTED LIST
'''
def sum(l):
    summ=0
    for i in l:
        if type(i)==list:
            summ+=sum(i)
        else:
            summ+=i
    return summ
'''
#print(sum([11,[20,[30,100],240],200]))

# 2  WAP FOR CONVERTING NESTED LIST INTO FLATTENED LIST
'''
def fltlst(l):
    el=[]
    for i in l:
        if type(i)==list:
            el.extend(fltlst(i))
        else:
            el.append(i)
    return el
#print(fltlst([11,[20,[30,100],240],200]))
'''