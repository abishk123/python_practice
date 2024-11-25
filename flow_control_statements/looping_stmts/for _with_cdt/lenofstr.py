# 1  WAP
'''
length = 0 # initially i'm assuming s as empty str
s = input('string : ') # taking str input from user






# 2  WAP TO PRINT HOW MANY TIMES THE GIVEN SUBSTRING IS PRESENT IN SPECIFIED STRING

c = 0  # if the substr is not there,assuming  substr count as 0 initially
string = input('str : ')  # taking str input from user
s_s = input('s_s : ')  # taking substring input from user
for i in string:  # extracting each and every element 
    if s_s == i:  # comparing substr is with element 
        c += 1  # we are adding 1 for every time when element is sameas substring else it skips/dont increment c
print(c)  # at last we are printing the count of substr in the given str


str = 'abhisheka'
s_s = 'a'

iteration : 1

i = a
now we are comparing i with sibstr(a)
its true,it will increment c value by 1(c=1)

iteration : 2

now we are comparing i(b) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 3

now we are comparing i(h) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 4

now we are comparing i(i) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 5

now we are comparing i(s) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 6

now we are comparing i(h) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 7

now we are comparing i(e) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 2

now we are comparing i(b) with sibstr(a)
its not true,it will not increment c value(c=1)

iteration : 2

now we are comparing i(b) with sibstr(a)
its not true,it will not increment c value(c=1)



# 3  WAP TO PRINT HOW MANY VOWELS ARE PRESENT IN THE GIVEN STRING

c = 0
v = ['a','e','i','o','u'] 
string = input('string : ')

for i in string:
    if i.lower() in v:
        c += 1
print(c)

# 4  WAP TO PRINT NO OF CONSONENTS PRESENT IN GIVEN STRING

c = 0
v = ['a','e','i','o','u'] 
string = input('string : ')

for i in string:
    if  i.isalpha() and i.lower() not in v:
            c += 1
print(c)
'''
# 5  find distinct element in the array

l = eval(input('list : '))
e_l = set()
for i in l:
    if i not in e_l:
        e_l.append(i)
print(e_l)

# 6  WAP TO FIND NO OF CHARS,SPECIAL CHARS, DIGITS

s = input()
c = 0
s_c = 0
d = 0
for i in s:
    if i
