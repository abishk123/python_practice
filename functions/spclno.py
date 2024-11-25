def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
   
    
#factorial(5)
def factorialNumbers(ll,ul):
    for n in range(ll,ul+1):
        f=factorial(n)
        return f

factorialNumbers(1,10)

def isSpecial(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        summ+= factorial(rem)
        dummy//=10
    if summ==n:
        return True
    else:
        return False
#s=isSpecial(40585)             
#print(s)
def specialNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isSpecial(n):
            print(n)        
        
#specialNumbers(1,100000)