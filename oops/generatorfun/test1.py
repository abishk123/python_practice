# GENERATOR FUNCTION FOR FIBONACCI SERIES
def fiboGen(a,b,n):
    i=1
    while i<=n:
        yield a
        a,b=b,a+b
        i+=1

FGO=fiboGen(2,3,10)
for i in FGO:
    print(i)

#MEMORY CONSUPTION IS MORE IN GENERATORS THAN ITERATORS