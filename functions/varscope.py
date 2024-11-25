'''
a=10 # global variable
def modify():
    global a
    print(a)
    a-=2
    print(a)

modify()

print(a)
'''
'''
def local():
    l=10
    print(l)
local()
print(l) # local var not accessed in main space
'''

def outer():
    a=10
    def inner():
        nonlocal a
        print(a)
        a-=2
        print(a)
    print(a)
    inner()
outer()



