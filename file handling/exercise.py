# 1. WAP TO PRINT HOW MANY LINES OF DATA WE HAVE IN GIVEN FILE

fo=open('sample1.txt','w')
fo.write('''WHAT IS LEXICAL SCOPE hai

1.THE VARIABLES, WHICH ARE CREATED OUTSIDE THE FUNCTION CAN BE ACCESSIBLE INSIDE THE FUNCTION(THIS IS CALLED PARENT SCOPE)
2.SO,LEXICAL SCOPE IS NOTHING BUT PARENT SCOPE

WHAT IS SCOPE CHAIN

1.WHEN A VARIABLE IS USED, JS WILL SEARCH FOR THAT VARIABLE IN CURRENT SCOPE, IF IT NOT FOUND THEN IT WILL LOOK INTO ITS PARENT SCOPE,THIS PROCESS CONTINIOUS UNTIL GLOBAL SCOPE(NULL)
2.SCOPE CHAINING IS POSSIBLE BCOZ OF LEXICAL ENVIRONMENT.
''')

fo.close()
fo=open('sample1.txt','r')
data1=fo.readlines()
print(data1)
print(len(data1[0]))
print(len(data1))
# 2. WAP TO PRINT HOW MANY WORDS OF DATA WE HAVE IN GIVEN FILE
fo=open('sample1.txt','r')
data=fo.read()
words=data.split()
print(words)
print(len(words))
# 3. WAP TO PRINT HOW MANY CHARACTERS OF DATA WE HAVE IN GIVEN FILE

fo=open('sample1.txt','r')
data=fo.read()
print(f'LENGTH OF DATA IS {len(data)}')
#print(fo.tell())
# 4. WAP TO PRINT HOW MANY LINES OF DATA WE HAVE IN GIVEN FILE WITH 80 CHARACTERS IN IT
count=0
for line in data1:
    if len(line)==80:
        count+=1
print(count)
# 5. WAP TO PRINT HOW MANY WORDS OF DATA WE HAVE IN GIVEN FILE WITH 5 CHARACTERS IN IT
c_o_w=0
for word in words:
    if len(word)==5:
        c_o_w+=1
print(c_o_w)

# 6. WAP TO PRINT HOW MANY WORDS OF DATA WE HAVE IN GIVEN FILE WHICH ARE STARTING WITH 'H'
c_o_h=0
for i in words:
    if i.startswith('H'):
        c_o_h+=1
print(c_o_h)
