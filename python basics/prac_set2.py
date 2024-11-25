# 6  WAP TO PRINT HOW MANY DIGITS IN THE GIVEN STRING
'''
s = input('string : ')  # taking string input from user
c_d = 0  # assuming that initially there is no digits in string
integer = '1234567890'  # storing all digits in a variable
for i in s: # extracting each and every element and assigning to i
  # if i.isdigit():
   if i in integer:
        c_d += 1
print(c_d)

iterations :
s = 'abhi123'

iteration : 1
i = a
now checking i(a) is present in integers
its false,it will not increment c_d value(c_d=0)
iteration : 2
i = b
now we are checking i(b) is present in integers
its false,it will increment c_d value by 1(c_d=1)
iteration : 3
i = h
now we are checking i(h) is present in integers
its false,it will not increment c_d value(c_d=0)
iteration : 4
i = i
now we are checking i(i) is present in integers
its false,it will increment c_d value by 1(c_d=1)
iteration : 5
i = 1
now we are checking i(1) is present in integers
its True,it will increment c_d value by 1(c_d=1)
iteration : 6
i = 2
now we are extracting i(2) is present in integers
its True,it will increment c_d value by 1(c_d=2)
iteration : 6
i = 3
now we are extracting i(3) is present in integers
its True,it will increment c_d value by 1(c_d=3)


'''
# 7  WAP TO PRINT HOW MANY EVEN DIGITS PRESENT IN GIVEN STRING
'''
s = input('s : ')
c_e = 0
for i in s:
    if i.isdigit():
        i = int(i)
        if i%2 == 0:
            c_e += 1
print(c_e)

s = input('s : ')
even = '02468'
for i in s:


# 8  WAP TO PRINT SUM OF DIGITS PRESENT IN THE GIVEN STRING

s = input('s : ')
total = 0 
for i in s:
    if i.isdigit():
        total += int(i)
print(total)

# 9  WAP TO PRINT SPECIAL CHARACTERS IN GIVEN STRING

s = input('s : ')
c_s_c = 0
for i in s:
    if i.isalnum() == False:
        c_s_c += 1
print(c_s_c)
'''
# 10  WAP TO PRINT SUM OF NUMBERS PRESENT IN A GIVEN LIST
'''
l = eval(input('list : '))
sum = 0
for i in l:
    if type(i)==int: #isinstance(element(i),class(int))
        # 
        sum += i
print(sum)
'''
# WAP TO PRINT THE FREQYENCY OF EACH AND EVERY ELEMENT OF A GIVEN STRING
#print sum of first n numbers
sum = 0
n = int(input('n:'))
for i in range(n+1):
    sum += i
print(sum)
