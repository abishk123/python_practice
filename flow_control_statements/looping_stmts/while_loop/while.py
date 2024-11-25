# 1  print sum of first n numbers
'''
n = int(input('n : '))
i=0
sum = 0
while i<n+1:
    sum+=i
    i += 1
print(sum)
'''
# 2  WAP TO PRINT FACTORIAL OF GIVEN NUMBER
'''
n = int(input('n : '))
i=1
fact = 1
while i<n+1:
    fact *= i
    i += 1
print(n,"! is ",fact)
'''

# 3  WAP TO PRINT GIVEN NUMBER IS PERFECT OR NOT
'''
n = int(input('n: '))
i = 1
sum=0
while i<n//2+1:
    if n%i==0:
        sum += i
    i +=1
if sum==n:
    print(sum,"is perfect number")
else:
    print('not perfect number')


ITERATIONS
N=8

ITERATION-1 i=1
IT WILL CHECK I(1) < N//2+1 {1<5}>>TRUE 
SO IT WILL AGAIN CHECK THAT N%I==0{8%1==0}>>TRUE
THEN,I(1) WILL BE ADDED TO SUM VARIABLE{SUM=O+1=1}
I = I+1 {1+1=2}
ITERATION-2 i=2
IT WILL CHECK I(2) < N//2+1 {2<5}>>TRUE 
SO IT WILL AGAIN CHECK THAT N%I==0{8%2==0}>>TRUE
THEN,I(2) WILL BE ADDED TO SUM VARIABLE{SUM=1+2=3}
I = I+1 {2+1=3}
ITERATION-3 i=3
IT WILL CHECK I(3) < N//2+1 {3<5}>>TRUE 
SO IT WILL AGAIN CHECK THAT N%I==0{8%3==0}>>FALSE
THEN,I(3) WILL NOT ADDED TO SUM VARIABLE
I = I+1 {3+1=4}
ITERATION-4 i=4
IT WILL CHECK I(4) < N//2+1 {4<5}>>TRUE 
SO IT WILL AGAIN CHECK THAT N%I==0{8%4==0}>>TRUE
THEN,I(4) WILL BE ADDED TO SUM VARIABLE{SUM=3+4=7}
I = I+1 {4+1=5}
ITERATION-5 i=5
IT WILL CHECK I(5) < N//2+1 {5<5}>>FALSE

SO,IT WILL COMEOUT FROM LOOP

AND IT WILL CHECK SUM WITH N(SUM==N)(7==8)>>FALSE
SO IT WILL PRINT ELSE STATEMENTS



'''
# 4  WAP TO PRINT EVEN NUMBERS IN A GIVEN RANGE
'''
ll=int(input('ll:'))
ul=int(input('ul:'))
while ll<ul+1:
    if ll%2==0:
        print(ll)
    ll+=1
'''
# 5  swap even indexed elements to odd indexed elements
'''
l = eval(input('l:')) 
ip=0
if len(l)%2==0:
    while ip<len(l):
        l[ip],l[ip+1]=l[ip+1],l[ip]
        ip += 2
    print(l)
else:
    print('give proper even no of elements')
'''
# 6  WAP TO PRINT REVERSE OF LIST
'''
l = eval(input('l:')) 
ip=0
while ip<=len(l)//2:
    l[ip],l[-(ip+1)]=l[-(ip+1)],l[ip]
    ip += 1
print(l)
'''
# print max number in list
# WAP TO PRINT THE SUM OF INDIVIDUAL DIGITS IN GIVEN NUMBER WITHOUT USING CONVERSION METHODS

n = int(input('n:'))
dummy=n
