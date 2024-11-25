'''p-1

*   
* *
* * *
* * * *
* * * * *

n = 5
stars = 1
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end= ' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=1
'''
'''
p-2
          *
        * *
      * * *
    * * * *
  * * * * *


n = 5
stars = 1
spaces = n
for row in range(1,n+1):
    for sp in range(1,spaces):
        print(' ',end= ' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=1
    spaces-=1
'''

'''
p-3
* * * * *
* * * *   
* * *   
* *    
*       
   

n = 5
stars = n
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces):
        print(' ',end= ' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1
'''
'''
p-4

* * * * *
  * * * *
    * * *
      * *
        *


n = 5
stars = n
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end= ' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1
    spaces+=1
'''
'''
p-5

*
  *
    *
      *
        *


n = 5
stars = 1
spaces = 0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end= ' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
'''
'''
p-6
        *
      * 
    *
  *
*

n = 5
stars = 1
spaces = n
for row in range(1,n+1):
    for sp in range(1,spaces):
        print(' ',end= ' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
'''
