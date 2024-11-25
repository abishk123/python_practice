# 1  WAP TO PRINT INDEX POSITIONS OF ALL THE VOWELS PRESENT IN THE GIVEN STRING
'''
s = input('s : ')
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        print(ip)
'''
# 2  WAP TO PRINT THAT ELEMENTS WHICH ARE PRESENT IN EVEN INDEX POSITIONS

#s=input('s:')
'''
for ip in range(len(s)):
    if ip%2==0:
        print(s[ip])

for ip in range(0,len(s),2):
    print(s[ip])
'''
# 3  find the sum of index positions of the digits present in given string

'''
s = input('s:')
summ=0
for ip in range(len(s)):
    if s[ip].isdigit(): # s[ip] in '0123456789'
        summ += ip
print(summ)
'''
# 4  WAP TO ADD INDEX POSITIONS OF EVEN NUMBERS IN A GIVEN STRING
'''
s = input('s:')
summ=0
for ip in range(len(s)):
    if s[ip] in '02468':
        summ += ip
print(summ)
'''

'''
s = input('s:')
summ=0
for ip in range(len(s)):
    if s[ip].isdigit() and int(s[ip])%2==0:
        summ += ip
print(summ)
'''
# 5  WAP TO FIND THE SUM OF EVEN DIGITS PRESENT IN EVEN INDEX POSITIONS IN A GIVEN STRING
'''
s = input('s : ')
sum = 0
for ip in range(len(s)):
    if s[ip].isdigit() and ip%2==0 and int(s[ip])%2 ==0:
        sum += int(s[ip])
print(sum)
'''
'''
s = input('s : ')
sum = 0
for ip in range(0,len(s),2):
    if s[ip] in '02468':
        sum += int(s[ip])
print(sum)
'''
# 6  HW-1:WAP TO FIND SUM OF EVEN IP OF EVEN DIGITS
'''
s = input('s : ') # TAKING STRING INPUT FROM USER
sum = 0 # ASSUMING THAT THERE IS NO EVEN NUMBERS AT EVEN INDEX POSITIONS
for ip in range(0,len(s),2): # EXTRACTING EACH AND EVERY EVEN INDEX POSITION OF GIVEN STRING
    if s[ip].isdigit() and int(s[ip])%2==0: # CHECKING THAT AT EVEN INDEXED VALUE IS EVEN DIGIT OR NOT
        sum += ip # IF THE ABOVE COND SATISFIES THEN THE RESPECTIVE INDEX POSITIONS IS ADDED TO SUM VARIABLE
print(sum) # ATLAST WE ARE PRINTING THE SUM OF EVEN INDEX POSITIONS HAS EVEN DIGITS
'''
'''ITERATIONS;
S = 'ABHI12356'

ITERATION -1 : IP = 1 ,S[1]=B
NOW WE WILL CHECK S[1]=B IS EVEN DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -2 : IP = 3 ,S[3]=I
NOW WE WILL CHECK S[3]=I IS EVEN DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -3 : IP = 5 ,S[5]=2
NOW WE WILL CHECK S[5]=2 IS EVEN DIGIT OR NOT
THE COND IS TRUE,WE WILL ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0+5=5)
ITERATION -4 : IP = 7 ,S[7]=5
NOW WE WILL CHECK S[7]=5 IS EVEN DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM (SUM=5)

THE ITERATIONS ARE ENDED BCOZ THERE IS NO ODD INDEX POSITION AFTER 7 IN THE GIVEN STRING

SUM = 7

'''
# 7  HW-2:WAP TO FIND SUM OF ODD IP OF EVEN DIGITS
'''
s = input('s : ') # taking string input from user
sum = 0 # assuming that there is no even numbers at odd index positions of given string
for ip in range(1,len(s),2): # ectracting each and every odd index positions of given str one by one
    if s[ip].isdigit() and int(s[ip])%2==0: # checking that the element at odd index positions is even number or not
        sum += ip # if above cond satisfies,then the respected index positions is added to sum variable
print(sum) # at last we are printing the sum of odd ip's of even numbers
'''
'''ITERATIONS;
S = 'ABHI12356'

ITERATION -1 : IP = 1 ,S[1]=B
NOW WE WILL CHECK S[1]=B IS EVEN DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -2 : IP = 3 ,S[3]=I
NOW WE WILL CHECK S[3]=I IS EVEN DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -3 : IP = 5 ,S[5]=2
NOW WE WILL CHECK S[5]=2 IS EVEN DIGIT OR NOT
THE COND IS TRUE,WE WILL ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0+5=5)
ITERATION -4 : IP = 7 ,S[7]=5
NOW WE WILL CHECK S[7]=5 IS EVEN DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM (SUM=5)

THE ITERATIONS ARE ENDED BCOZ THERE IS NO ODD INDEX POSITION AFTER 7 IN THE GIVEN STRING

SUM = 7

'''
'''
# 8  HW-3:WAP TO FIND SUM OF ODD IP OF ODD DIGITS

s = input('s : ') # taking string input from user
sum = 0  # asssuming that there is no odd digits in odd index positions
for ip in range(1,len(s),2): # extracting each and every odd index position value(or)element of given string
    if s[ip].isdigit() and int(s[ip])%2!=0: # checking that the element is odd number or not
        sum += ip # if the element is odd number,then we are adding its respective index position into sum named variable
print(sum) # at last we are printing the sum of odd ip of odd digits
''''''
ITERATIONS;
S = 'ABHI12356'

ITERATION -1 : IP = 1 ,S[1]=B
NOW WE WILL CHECK S[1]=B IS ODD DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -2 : IP = 3 ,S[3]=I
NOW WE WILL CHECK S[3]=I IS ODD DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -3 : IP = 5 ,S[5]=2
NOW WE WILL CHECK S[5]=2 IS ODD DIGIT OR NOT
THE COND IS FALSE,WE WILL NOT ADD ITS RESPECTIVE INDEX POSITION TO SUM(SUM=0)
ITERATION -4 : IP = 7 ,S[7]=5
NOW WE WILL CHECK S[7]=5 IS ODD DIGIT OR NOT
THE COND IS TRUE,WE WILL ADD ITS RESPECTIVE INDEX POSITION TO SUM (SUM+=7)

THE ITERATIONS ARE ENDED BCOZ THERE IS NO ODD INDEX POSITION AFTER 7 IN THE GIVEN STRING

SUM = 7

'''


# 9  WAP TO PRINT THE MAX NUMBER IN A GIVEN LIST AND ITS INDEX POSITION
'''
l = eval(input('list : '))
max = l[0]
mip = 0
for ip in range(1,len(l)):
    if l[ip]> max:
        max = l[ip]
        mip = ip
print(max,mip)




l = eval(input('list : '))
max = 0
for ip in range(len(l)):
    if l[ip]> max:
        max = l[ip]

print("at index position ",l.index(max)," max value is ",max)
'''
# 10  WAP TO PRINT HOW MANY TIMES THE GIVEN SUBSTRING IS PRESENT IN SPECIFIED STRING
'''
m_s = input('m_s : ')
s_s = input("s_s : ")
c = 0
for ip in range(len(m_s)-len(s_s)+1):
    if m_s[ip:ip+len(s_s)]==s_s:
        c += 1
print(c)
'''
'''
#  check each and every digit is even or not if all digits are even then only print that number
l = []
for n in range(100,401):
    if int(str(n)[-1])%2==0 and int(str(n)[-2])%2==0 and int(str(n)[-3])%2==0:
        l.append(n)
print(l)
'''

for i in range(100,401):
    s=str(i)
    c=0
    for ip in range(len(s)):
        if int(s[ip])%2==0:
            c+=1
        else:
            break
    if len(s)==c:
        print(i,end=',')
    




# 11  swap even indexed element with adjacent odd indexed element
'''
l = eval(input('l:'))
if len(l)%2==0:
    for ip in range(0,len(l),2):
        l[ip],l[ip+1]=l[ip+1],l[ip]
    print(l)
else:
    print('give even length list')

# 12  convert [11,22,33,100,44] into [44,100,33,22,11]

l= eval(input('l : '))

for ip in range(0,(len(l))//2):
    l[ip],l[-(ip+1)]=l[-(ip+1)],l[ip]
print(l)

    '''

