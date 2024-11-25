class FiboIterator():
    def __init__(self,fv,sv,n):
        self.fv=fv
        self.sv=sv
        self.n=n

    def __iter__(self):
        self.i=1 # traversing starts from 1 -  n
        return self
    def __next__(self):
        if self.i <= self.n:
            res=self.fv
            self.fv,self.sv=self.sv,self.fv+self.sv
            self.i+=1
            return res
        raise StopIteration
    
FIO=FiboIterator(2,3,10)
print(list(FIO))

print(FIO)
for i in FIO:
    print(i)


class IteratorClass():
    def __init__(self,ll,ul,up):
        self.ll=ll
        self.ul=ul
        self.up=up
    def __iter__(self):
        self.i=self.ll
        return self
    def __next__(self):
        if self.ll<self.ul:
            res=self.ll
            self.ll+=self.up
            return res
        raise StopIteration
ICO=IteratorClass(1,5,1)
for i in ICO:
    print(i)


class PowerIteratorClass():
    def __init__(self,ll,ul,up):
        self.ll=ll
        self.ul=ul
        self.up=up
    def __iter__(self):
        self.i=self.ll
        return self
    def __next__(self):
        if self.ll<self.ul:
            res=self.ll**3
            self.ll+=self.up
            return res
        raise StopIteration
PICO=PowerIteratorClass(1,5,1)
for i in PICO:
    print(i)