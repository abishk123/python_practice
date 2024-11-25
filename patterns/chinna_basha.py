'''
1 
  2 
    3 
  5 
4 
n=7
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row<=n//2:
            dummy+=1
            spaces+=1
        elif row==n//2+1:
            dummy+=n//2
            spaces-=1
        else:
            dummy-=1
            spaces-=1
    print()
 '''           
'''
1 
  3 
    5 
      7 
    6 
  4 
2 
n=7
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row<=n//2:
            dummy+=2
            spaces+=1
        elif row==n//2+1:
            dummy-=1
            spaces-=1
        else:
            dummy-=2
            spaces-=1
    print()
'''

'''
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(pri[ip],end=' ')
        ip+=1
        if row<=n//2:
            spaces+=1
        else:
            spaces-=1
    print()
    
'''
'''
#PRIME NUMBERS
2 
  3 
    5 
  7 
11 
num=int(input('num:'))
pri=[]
n=1
c=0
ip=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            c+=1
            pri.append(n)
            if c==num:
                break
    n+=1

spaces=0
stars=1
for row in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        if ip<num:
            print(pri[ip],end=' ')
            ip+=1
        if row<=num//2:
            spaces+=1
        else:
            spaces-=1
    print()
'''
num=int(input('num:'))
fib=[]
a=0
b=1
count=0
fib.append(a)
fib.append(b)
while True:
    c = a + b
    a,b=b,c
    fib.append(c)
    count+=1
    if count==num:
        break
print(fib)
        

