'''
p-1

p  

p  y  

p  y  t  

p  y  t  h  

p  y  t  h  o  

p  y  t  h  o  n

st=input('str:')
n=len(st)
s=''
for row in range(1,n+1):
    s=s+st[row-1]+'  '
    print(s)
    print()
'''
'''
column-wise 
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 


n=int(input('n:'))
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    
  '''
'''
col_wise-inc & carried to next row
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 

n=int(input('n:'))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()  
'''




'''
#ROW-WISE-INCREMENTATION AND INCREMENTED VALUE IS CARRIED TO NEXT ROW
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
n=int(input('n:'))
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
    print()
    dummy+=1
'''
'''
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
n=int(input('n:'))
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    
'''
'''
1 6 11 16 21 
2 7 12 17 22 
3 8 13 18 23 
4 9 14 19 24 
5 10 15 20 25 


n=int(input('n:'))
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=5
    print()
'''
'''
1 2 3 4 5 
2 4 6 8 10 
3 4 5 6 7 
4 6 8 10 12 
5 6 7 8 9 


n=int(input('n:'))
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy+=2
        else:
            dummy+=1
    print()
'''
#ALPHABETS
'''
n=int(input('n:'))
stars=1
spaces=n-1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if dummy==26:
            dummy=0
        dummy+=1
    print()
    stars+=1
    spaces-=1
    
'''
n=5
spaces=0
stars=1


for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+=1):
        print(dummy,end=' ')
    if 

    
