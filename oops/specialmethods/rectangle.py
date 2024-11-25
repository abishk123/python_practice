class Rectangle():
    def __init__(self,length,breadth):
        self.rlength=length
        self.rbreadth=breadth
    def __mul__(self):
        return self.rlength*self.rbreadth
    def __gt__(self,secondobject):
        return self.rlength*self.rbreadth>secondobject.rlength*secondobject.rbreadth
    
r1=Rectangle(20,40)
r2=Rectangle(30,40)
print(r1<r2)

'''
class Rectangle():
    def __init__(self,length,breadth):
        self.rlength=length
        self.rbreadth=breadth
        self.rarea=self.rlength*self.rbreadth
    #def __mul__(self):
     #   return self.rlength*self.rbreadth
    def __gt__(self,secondobject):
        return self.rarea>secondobject.rarea
    
r1=Rectangle(20,40)
r2=Rectangle(30,40)
print(r1<r2)
'''