'''p-1

*
* *
* * *
* * * *
* * * * *
'''

n=10
'''
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()
'''
'''
for rows in range(1,n+1):
    print('* '*rows)
'''
'''
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
p-2
          *
        * *
      * * *
    * * * *
  * * * * *

for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
p-3
* * * * * *
* * * * *   
* * * *   
* * *    
* *      
*          
  
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
'''
p-4

* * * * *
  * * * *
    * * *
      * *
        *
'''
'''
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
p-5
*
  *
    *
      *
        *
'''        '''
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
'''
p-6
        *
      * 
    *
  * 
*
'''
'''
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
p-7

* * * * * * *
* *       * *
*   *   *   *
*     *     *
*   *   *   *
* *       * *
* * * * * * *
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1 or row==1 or row==n or col==1 or col==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
