def reverse(n):
    rev=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        rev=rev*10+rem
        dummy//=10
    return rev


def isPalindrome(n):
    if n==reverse(n):
        return True
    else:
        return False

    
def isPrime(n):
    if n>1:
        for i in range(2, n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False


def isPaliPrime(m):
    rev=reverse(m)
    if rev==m and isPrime(m):
        return True
    else:
        return False
def paliPrimeNumbers(LL,UL):
    for i in range(LL,UL+1):
        if isPaliPrime(i):
            print(i)
            
            
#paliPrimeNumbers(1,1000)
def length(n):
    dummy=n
    l=0
    while dummy>0:
        l+=1
        dummy//=10
    return l    
def isDisarium(n):
    dummy=n
    summ=0
    l=length(n)
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        l-=1
        dummy//=10
    if summ==n:
        return True
    else:
        return False
       
       
def disariumNumbers(ll,ul) :
    for n in range(ll,ul+1):
        if isDisarium(n):
            print(n)
   
#disariumNumbers(1,1000)
def isArmstrong(n):
    l=length(n)
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        dummy//=10
    if summ==n:
        return True
    else:
        return False    
        
        
def armstrongNumbers(ll,ul) :
    for n in range(ll,ul+1):
        if isArmstrong(n):
            print(n)
            
#armstrongNumbers(1,1000)                

          
def isHarshad(n):
    summ=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        summ+=rem
        dummy//=10
    if n%summ==0:
        return True
    else:
        return False

                           
def harshadNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isHarshad(n):
            print(n)
            
                        
#harshadNumbers(100,200)


def isPerfect(n):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if n==summ:
        return True
    else:
        return False

 
def perfectNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isPerfect(n):
            print(n)
            
            
#perfectNumbers(1,150)


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
    
    
#factorial(5)
def factorialNumbers(ll,ul):
    for n in range(ll,ul+1):
        f=factorial(n)
        print(f)
factorialNumbers(1,20)
'''
def isSpecial(n):
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum+=factorial(rem)
        dummy//=10
    if sum==n:
        return True
    else:
        return False
                

def specialNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isSpecial(n):
            print(n)        
        
specialNumbers(1,1000)        
'''