#ARMSTRONG NUMBERS IN BETWEEN TWO LIMITS
# 153=1**3 + 5**3 + 3**3 = 153, 9 = 9**1 = 9
'''
ll=int(input('ll:'))
ul=int(input('ul;'))
armstrongs = []
while ll<ul:
    n=ll
    ll+=1
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum+=rem**len(str(n))
        dummy//=10
    if sum==n:
        armstrongs.append(n)
print('armstrongs are ',armstrongs)


ll=int(input('ll:'))
ul=int(input('ul;'))
while ll<ul:
    n=ll
    ll+=1
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum+=rem**len(str(n))
        dummy//=10
    if sum==n:
        print(n)



ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    l=len(str(n))
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if n==sum:
        print(n)
'''
# WAP TO PRINT EVERY 2ND ARMSTRONG NUMBER IN THE GIVEN RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
c=0
for n in range(ll,ul+1):
    l=len(str(n))
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if n==sum:
        c+=1
        if c%2==0:
            print(n)
'''
# WAP TO PRINT EVERY 3rd ARMSTRONG NUMBER IN THE GIVEN RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
c=0
for n in range(ll,ul+1):
    l=len(str(n))
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum+=rem**l
        dummy//=10
    if n==sum:
        c+=1
        if c%3==0:
            print(n)
'''
# WAP TO PRINT PERFECT NUMBERS IN A RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    i = 1
    sum=0
    while i<n//2+1:
        if n%i==0:
            sum += i
        i +=1
    if sum==n:
        print(n)
'''
# WAP TO PRINT 2nd PERFECT NUMBERS IN A RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
c=0
for n in range(ll,ul+1):
    i = 1
    sum=0
    while i<n//2+1:
        if n%i==0:
            sum += i
        i +=1
    if sum==n:
        c+=1
        if c%2==0:
            print(n)    
'''
# WAP TO PRINT PERFECT NUMBERS IN A RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
c=0
for n in range(ll,ul+1):
    i = 1
    sum=0
    while i<n//2+1:
        if n%i==0:
            sum += i
        i +=1
    if sum==n:
        c+=1
        if c%3==0:
           print(n)
'''



# DISARIUM NUMBERS BETWEEN TWO LIMITS
#
'''
ll=int(input('ll;'))
ul = int(input('ul:'))
disariums=[]
while ll<ul:
    n=ll
    ll+=1
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem = dummy%10
        summ += rem**l
        l-=1
        dummy//=10
    if n==summ:
        disariums.append(n)
print('disarium numbers are ',disariums)

# HARSHAD NUMBERS BETWEEN TWO LIMITS

ll=int(input('ll;'))
ul = int(input('ul:'))
harshads=[]
while ll<ul:
    n=ll
    ll+=1
    dummy=n
    summ=0
    l=len(str(n))
    while dummy>0:
        rem = dummy%10
        summ += rem
        dummy//=10
    if n%summ==0:
        harshads.append(n)
print('harshads are ',harshads)

# PRIME NUMBERS BETWEEN TWO LIMITS

ll=int(input('ll:'))
ul=int(input('ul:'))
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)


'''

# WAP TO PRINT EVERY 2ND PRIME NUMBER IN A GIVEN RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
l=[]  # THIS APPROACH CONSUMES MORE MEMORY
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            l.append(n)
for ip in range(len(l)):
    if ip%2!=0:
        print(l[ip])


ll=int(input('ll:'))
ul=int(input('ul:'))
c=0
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            c+=1
            if c%2==0:
                print(n)


# WAP TO PRINT EVERY THIRD PRIME NUMBER IN A GIVEN RANGE

ll=int(input('ll:'))
ul=int(input('ul:'))
c=0
for n in range(ll,ul+1):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            c+=1
            if c%3==0:
                print(n)
'''