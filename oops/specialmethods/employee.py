class Employee():
    c_name='abc'
    c_location='bengaluru'
    emp_count=0
    def __init__(self,en,ea,er,es):
        self.e_name=en
        self.e_age=ea
        self.e_role=er
        self.e_salary=es
        Employee.emp_count+=1
    
    def __str__(self):
        return self.e_name
    
    def __del__(self):
        Employee.emp_count-=1
        print(f'{self} is resigned')
        
raj=Employee("raja reddy",29,"trainee",30000)
print(raj)
print(Employee.emp_count)
print(raj)