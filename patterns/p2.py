'''
p-1
       * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *



rows=5
cols=(2*rows)-1
stars=1
spaces=cols//2
for row in range(1,rows+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1

n=5
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1
'''
'''
p-2
* * * * * * * 
  * * * * * 
    * * * 
      * 

n=4
stars=(2*n)-1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=2
    spaces+=1
'''
'''
p-3

* 
* * * 
* * * * * 
* * * 
* 

n=5
stars=1
spaces=0
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end=' ')    
    print()
    if row<=n//2:
        stars+=2
    else:
        stars-=2
  '''
'''
p-4
    

      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      *
'''

n=5
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1







'''
n=4
stars=1
spaces=n-1
for row in range(1,n):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=2
    spaces+=1

'''













