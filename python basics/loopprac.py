# 1  WAP TO CHECK THE NUMBER IS PRIME OR NOT
'''
n=int(input('n:'))
if n>1:
    i=2
    while i < n//2+1:
        if n%i==0:
            print('not a prime')
            break
        i+=1
    else:
        print('prime')
else:
    print('not prime')

n=int(input('n:'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,' is not a prime')
            break
        i+=1
    else:
        print(n,' is prime')
else:
    print(n,' not prime')
'''
# 2  WAP TO REVERSE A STRING WITHOUT USING SLICING
'''
# APPROACH 1-- using negative index positions
s = input('s:')
rev=''
for ip in range(-1,-(len(s)+1),-1):
    rev+=s[ip]
print(rev)


# APPROACH 2--using normal approach
s = input('s:')
rev=''
for ele in s:
    rev=ele+rev
print(rev)
#using slicing
s=input()
print(s[::-1])

'''
# WAP TO GET FIBONACCI SERIES FROM A NUMBER TO ANOTHER NUMBER

