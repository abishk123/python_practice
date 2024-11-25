# 1.A  WAP TO PRINT 1ST 100 ARMSTRONG NUMBERS
'''
c=0
n=1
while c<15:
    sum=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if sum==n:
        c+=1
        print(n)
    n+=1

'''


# 1.B  WAP TO PRINT 15th ARMSTRONG NUMBER
'''
c=0
n=1
while c<15:
    sum=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if sum==n:
        c+=1
        if c==15:
            print(n)
    n+=1
'''
# 1.C  WAP TO PRINT ARMSTRONG NUMBERS IN A RANGE
'''
for n in range(1,10000):
    sum=0
    dummy=n
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if sum==n:
        print(n)

'''
# WAP TO CHECK THE GIVEN NUMBER IS DISARIUM OR NOT

'''THE GIVEN NUMBER IS EQUALS TO SUM OF INDIVIDUAL DIGIT TO THE POWER OF ITS POSITION
247 != 2**1 + 4 ** 2 + 7**3 SO 243 IS NOT A DISARIUM'''
'''
n=int(input('n:'))
dummy=n
summ=0
for ip in range(-1,-(len(n)))
while dummy>0:
    rem=dummy%10
    summ += rem**len(str(n))
  '''  


# 2 WAP TO CHECK THE GIVEN NUMBER IS SPECIAL NUMBER OR NOT

# 2.A WAP TO PRINT SPECIAL
        
# print largest number and smallest number in list
'''
lis = eval(input('list:'))
max=-99999999999999
for ele in lis:
    if ele>max:
        max=ele
print(max,' is the maximum number in the list')

min=max
for e in lis:
    if e<min:
        min=e
print(min,' is the minimum number in the list')
'''
lis = eval(input('list:'))
max=0



# wap to display sum of odd number and even number in a given range
'''
ll=int(input('ll:'))
lower=ll
ul=int(input('ul:'))
even_sum=0
odd_sum=0
while ll<=ul:
    if ll%2==0:
        even_sum += ll
    else:
        odd_sum += ll
    ll+=1
print(even_sum,f' is the sum of even numbers from {lower} to {ul}')
print(odd_sum,f' is the sum of even numbers from {lower} to {ul}')
'''
# WAP TO DISPLAY ALL NUMBERS WHICH ARE DIVISIBLE BY 13 BUT NOT BY 3 BETWEEN 
# GIVEN LIMITS AND EXCLUDE THAT LIMITS
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll+1,ul):
    if n%13==0 and n%3!=0:
        print(n)
'''
# WAP TO PRINT THE SUM OF SEQUENCE 1+1/1!+1/2!+1/3!...UPTO 1/N!

# WAP TO PRINT NUMBERS WHICH HAS BELOW 4 FACTORS

ll=int(input('ll:'))
ul=int(input('ul:'))
print('2!','3!')
for n in range(ll,ul+1):
    if n<2:
        continue
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        print(n,n**2)

