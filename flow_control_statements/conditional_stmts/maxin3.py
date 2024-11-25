a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

'''
if a>b:
    if a>c:
        print('a is max')
    else:
        print('c is max')
else:
    if b>c:
        print('c is max')
    else:
        print('b is max')
        '''

d = int(input('d : '))
'''
if a>b:
    if a>c:
        if a>d:
            print('a is max')
        else:
            print('d is max')
    else:
        if c>d:
            print('c is max')
        else:
            print('d is max')
else:
    if b>c:
        if b>d:
            print('b is max')
        else:
            print('d is max')
    else:
        if c>d:
            print('c is max')
        else:
            print('d is max')

        
'''
# max among 5 numbers
e = int(input('e : '))

if a>b:
    if a>c:
        if a>d:
            if a>e:
                print('a is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
    else:
        if c>d:
            if c>e:
                print('c is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
else:
    if b>c:
        if b>d:
            if b>e:
                print('b is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
    else:
        if c>d:
            if c>e:
                print('c is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
