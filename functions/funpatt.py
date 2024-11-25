def butterFlyPattern(n):
    spaces=n-2
    stars=1
    for row in range (1,n+1):
        for st in range (1,stars+1):
            print ('*', end=' ')
        for sp in range (1,spaces+1):
            print('-',end=' ')
        for st in range (1,stars+1):
            print('*',end=' ')
        if row>=n//2+1:
            stars-=1
            spaces+=2
        elif row<n//2:
            stars+=1
            spaces-=2
        else:
            pass
        print()
butterFlyPattern(17)

#butterFlyPattern(16)
def box(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            if row==1 or col==1 or col==n or row==n:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

box(10)