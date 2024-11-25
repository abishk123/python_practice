'''
s=input()
s=s.split()
print(s,type(s))
new=[]
for i in s:
    new.append(int(i))

print(new)
'''
'''
l=input().split()
print(list(map(int,l)))
'''
'''
l=input()
print(list(map(int,l.split())))
'''
'''
#int values in list
l=[1,'11',12,'13',4]
print(list(filter(lambda x:int(x)==x,l)))
'''
from functools import reduce
l=[1,'11',12,'13',4]
print(reduce(lambda x,y:int(x)+int(y),l))