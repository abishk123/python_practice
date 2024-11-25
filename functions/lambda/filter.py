# WAP TO PRINT PRIME NUMBERS AND ARMSTRONG NUMBERS FROM THE GIVEN LIST
'''
def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
    
def isArmstrong(n):
    dummy=n
    sum=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if sum==n:
        return True
    else:
        return False

    
l=list(map(int,input('ip:').split()))
#print(list(filter(isPrime,l)))
print(f'prime list is : {list(filter(isPrime,l))}')
#print(list(filter(isArmstrong,l)))
print(f'armstrong list is : {list(filter(isArmstrong,l))}')
'''
# WAP TO CHECK THE GIVEN NUMBER IS PRIME OR NOT IN A SINGLE LINE(LAMBDA)

# WAP TO PRINT MAX VAL IN THE GIVEN LIST USING REDUCE FUNCTION
from functools import reduce

L=[11,2,33,44,55,66,44,77]

print(f'max is {reduce(lambda x,y:x if x>y else y,L)}')

print(f'min is {reduce(lambda x,y:x if x<y else y,L)}')

l=[[11,222,33],[2,3,4],[5,6,77,88]]

print(f'flat list is {reduce(lambda x,y:x+y,l)}')
print(f'total is {reduce(lambda x,y:x+y,L)}')


a=lambda x,y:x+y
print(a(10,20))