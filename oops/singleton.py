# USING EMPTY LIST
'''
def singleton(arg):
    l=[]
    def inner():
        if not l:
            mco=arg()
            l.append(mco)
        return l[0]
    return inner

@singleton
class Multiplex:
    def __init__(self):
        self.tickets=200
    def booking(self,n):
        if n<=self.tickets:
            self.tickets-=n
            print(f'{n} tickets are booked')
        else:
            print(f'{n} tickets are not available')
        print(f'{self.tickets} tickets are available')

gangu=Multiplex()
gangu.booking(100)
print(gangu)
satti=Multiplex()
satti.booking(20)
print(satti)
'''
# USING DICTIONARY

def singleton(arg):
    d={}
    def inner():
        if not d:
            d[arg]=arg()
        return d[arg]
    return inner

@singleton
class Multiplex:
    def __init__(self):
        self.tickets=200
    def booking(self,n):
        if n<=self.tickets:
            self.tickets-=n
            print(f'{n} tickets are booked')
        else:
            print(f'{n} tickets are not available')
        print(f'{self.tickets} tickets are available')

gangu=Multiplex()
gangu.booking(100)
print(gangu)
satti=Multiplex()
satti.booking(20)
print(satti)