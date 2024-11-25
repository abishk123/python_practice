
a = 10
b = 20
c = 10
print(id(a),a)
print(id(b),b)
print(id(c),c)

#
b = 25
print(id(b),b)
#
p,q,r,s = 50,60,70,65
print('p = ', p)
print('q = ', q)
print('r = ', r)
print('s = ', s)

print(id(p),p)
p = 90
print(id(p),p)

a, b = b, a
print(id(a),a)
print(id(b),b)


z = 22
#z = l #error
l = z
print(l)
print('bye')


