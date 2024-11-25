'''
p-1
  1 
  1 2 
  1 2 3 
  1 2 3 4 
  1 2 3 4 5 
1.COLUMN WISE INCERMENT --INCERMENTATION SHOULD BE INSIDE INNER LOOP
2.VALUE IS NOT CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE INSIDE OUTER LOOP
3.PATTERN IS WE ARE PRINTING AND INCERMENTING ONLY WHEN ROW IS LESSTHAN OR EQUALS TO COLUMN

n=5
spaces=0
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,n+1):
        if col<=row:
            print(dummy,end=' ')
            dummy+=1
    print()
'''
'''
p-2
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
1.COLUMN WISE INCERMENT --INCERMENTATION SHOULD BE INSIDE INNER LOOP
2.VALUE IS CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE OUTSIDE OF OUTER LOOP
3.PATTERN IS WE ARE PRINTING AND INCERMENTING ONLY WHEN ROW IS LESSTHAN OR EQUALS TO COLUMN

n=5
dummy=1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,n+1):
        if col<=row:
            print(dummy,end=' ')
            dummy+=1
    print()
'''
'''
p-3
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
1.ROW WISE INCERMENTATION --INCERMENTATION SHOULD BE OUTSIDE INNER LOOP(INSIDE OUTER LOOP)
2.VALUE IS CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE OUTSIDE OF OUTER LOOP
3.PATTERN IS WE ARE PRINTING AND INCERMENTING ONLY WHEN ROW IS LESSTHAN OR EQUALS TO COLUMN
n=5
spaces=0
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,n+1):
        if row >= col:
            print(dummy,end=' ')
    print()
    dummy+=1
'''
'''
P-4
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
1.ROW WISE INCERMENT --INCERMENTATION SHOULD BE OUTSIDE INNER LOOP
2.VALUE IS CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE OUTSIDE OF OUTER LOOP
3.PATTERN IS WE ARE PRINTING ONLY WHEN ROW + COL IS EQUALS OR LESSTHAN  N+1

n=5
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print(dummy,end=' ')
    print()
    dummy+=1
'''
'''
P-5
0 1 2 3 4 5 
0 1 2 3 4
0 1 2 3
0 1 2
0 1
1.COLUMN WISE INCERMENT --INCERMENTATION SHOULD BE INSIDE INNER LOOP
2.VALUE IS NOT CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE INSIDE OF OUTER LOOP
3.PATTERN IS WE ARE PRINTING ONLY WHEN ROW + COL IS EQUALS OR LESSTHAN  N+1

n=5
for row in range(1,n+1):
    dummy=0
    for col in range(0,n+1):
        if row+col<=n+1:
            print(dummy,end=' ')
            dummy+=1
    print()
'''
'''
p-6
1 
3 3
5 5 5
7 7 7 7
9 9 9 9 9
1.ROW WISE INCERMENT --INCERMENTATION SHOULD BE OUTSIDE OF INNER LOOP
2.VALUE IS CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE OUTSIDE OF OUTER LOOP
3.PATTERN IS WE ARE PRINTING ONLY WHEN ROW IS EQUALS OR greaterthan COLUMN
n=5
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row >=col:
            print(dummy,end=' ')
    print()
    dummy+=2
    '''
'''
p-7
        1 
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
1.ROW WISE INCERMENT --INCERMENTATION SHOULD BE OUTSIDE OF INNER LOOP
2.VALUE IS CARRIED TO NEXT ROW --VALUE CREATION SHOULD BE OUTSIDE OF OUTER LOOP
3.PATTERN IS WE ARE PRINTING AFTER SPACES,SO WE WRITE CODE FOR SPACES FIRST

n=5
dummy=1
spaces=n//2+1
numbers=1
for row in range(1,n+1):
    for sp in range(spaces+1):
        print(' ',end=' ')
    for col in range(1,numbers+1):
        print(dummy,end=' ')
    print()
    dummy+=1
    spaces-=1
    numbers+=2
'''
n=5
spaces=n//2
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for col in range(1,dummy+1):
        print(dummy,end=' ')
    print()
    if row<=n//2:
        dummy+=2
        spaces-=1
    else:
        dummy-=2
        spaces+=1