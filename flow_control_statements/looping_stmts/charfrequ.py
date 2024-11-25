# WAP TO PRINT THE FREQYENCY OF EACH AND EVERY ELEMENT OF A GIVEN STRING
# APPROACH 1:---WITHOUT USING METHOD
'''
s = input('s:')
d = {}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
'''
# APPROACH 2:---USING SET,COUNT METHOD
'''
s = input('s:')
for i in set(s):
    print(i,s.count(i))
'''
# APPROACH : 3--USING DICTIONARY AND METHODS

s = input('s : ')
d = {}
for i in s:
    if i not in d:
        d[i]=s.count(i)
print(d)



