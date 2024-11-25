#relation b/w 4 numbers
'''
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
d = int(input('d : '))
if  a==b==c==d:
    print('all are equal')
elif a>b and a>c and a>d:
    print('a is greater than all')
elif b>c and b>d:  #eliminating a
    print('b is greater than all')
elif c>d:   #eliminating b
    print('c is greater than all')
else:
    print('d is greater than all')
'''

# which is greater among 4 numbers

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
d = int(input('d : '))

if a>b and a>c and a>d:
    print('a is greater than all')
elif b>c and b>d:  #eliminating a
    print('b is greater than all')
elif c>d:   #eliminating b
    print('c is greater than all')
else:
    print('d is greater than all')


# r/n b/w 5 numbers

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
d = int(input('d : '))
e = int(input('e : '))

if  a==b==c==d==e:
    print('all are equal')
elif a>b and a>c and a>d and a>e:
    print('a is greater than all')
elif b>c and b>d and b>e:  #eliminating a
    print('b is greater than all')
elif c>d and c>e:   #eliminating b
    print('c is greater than all')
elif d>e:
    print('d is greater than all')
else:
    print('e is greater than all')