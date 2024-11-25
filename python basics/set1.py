'''
l = []


for i in range(100,400+1):
    for k1 in (str(i)):
        if int(k1)%2==0 :
            print(k1,'',k2,'',k3,',')


    '''

b_c=input('bc:') 
decimal=0
for ip in range(-1,-(len(b_c)+1)):
    if int(b_c[ip])==1:
        decimal += 2 ** ip-1
        print(decimal)