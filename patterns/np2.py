'''     1 
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5

n=5
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if st>stars//2:
            dummy+=1
        else:  #st<=stars//2
            dummy-=1
    print()
    stars+=2
    spaces-=1
'''
'''
5 5 5 5 5 
5 4 4 4 4
5 4 3 3 3
5 4 3 2 2
5 4 3 2 1
n=5
stars=n
for row in range(1,n+1):
    dummy=n
    for st in range(1,stars+1):
        print(dummy,end=' ')
        if row>st:
            dummy-=1
    print()
    '''
'''
        A 
      A B
    A B C
  A B C D
A B C D E
n=5
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    spaces-=1
    stars+=1
'''
'''
E E E E E 
E D D D D
E D C C C
E D C B B
E D C B A
n=5
stars=n
for row in range(1,n+1):
    dummy=n
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if row>st:
            dummy-=1
    print()
'''
'''
        A 
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
n=5
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=row
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
        if st<=stars//2:
            dummy-=1
        else:
            dummy+=1
    print()
    spaces-=1
    stars+=2
'''
n=10
stars=n
for row in range(1,n+1):
    for st in range(1,stars+1):
        if row==st:
            dummy=row
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()

