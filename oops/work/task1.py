# SINGLE-LEVEL-INHERITANCE
'''
class Xyz:
    company_name="xyz"
    empcount=0
    def __init__(self,name,age,sal,role):
        self.name=name
        self.age=age
        self.salary=sal
        self.designation=role
        Xyz.empcount+=1
    @classmethod
    def xyz_details(cls):
        print(f'NAME of company is {cls.company_name}')
        print(f'{Xyz.empcount} employees are working here')
    #object method
    def emp_details(self):
        print(f'name of emp is {self.name}')
        print(f'age of emp is {self.age}')
        print(f'sal of emp is {self.salary}')
        print(f'role of emp is {self.designation}')
    def __del__(self):
        Xyz.empcount-=1
    def __str__(self):
        return self.name
    #child class
class Manager(Xyz):
    def __init__(self,name,age,sal,role,dept,mno):
        super().__init__(name,age,sal,role)
        self.d_name=dept
        self.contact=mno
    def emp_details(self):
        super().emp_details()
        print(f'dept name is {self.d_name}')
        print(f'contact is {self.contact}')

abi=Xyz("ABHISHEK",23,500000,"S/W DEVELOPER")
nan=Xyz("NANI",25,60000,"TESTING")
sur=Manager("SURIYA",30,100000,'AUDITOR',"ACCOUNTING",6655443322)
nit=Manager("NITISH",23,60000,"RECRUITER","HR",63636363)
Xyz.xyz_details()#CLS OBJECT GENERIC DETAILS
nit.emp_details()#object method
print(nit)
'''
# MULTIPLE-INHERITANCE
'''
class Daddy():
    bike='ROYAL ENFIELD'
    house='3BHK'
    cash='10000'
    def behaviour():
        print("dad behaviour")
class Ma():
    wealth='7weaks gold'
    cash="200000"
    def behaviour():
        print("ma behaviour")
class child(Daddy,Ma):
    bike="Harley Davidson"
ab=child()
child.behaviour()
print(child.mro())
ab.behaviour()#error ,can  we access parent cls methods with child cls object or not
'''
# HIERARCHICAL-INHERITANCE
# 1 parent class, multiple child classes
'''
class Company:
    def __init__(self,name,addr,emp_count):
        self.name=name
        self.address=addr
        self.employee_count=emp_count

    def company_details(self):
        print(f'COMPANY NAME IS {self.name}')
        print(f'COMPANY ADDRESS IS {self.address}')
        print(f'TOTAL EMPLOYEES = {self.employee_count}')

class ItDepartment(Company):
    def __init__(self,name,addr,emp_count,projects):
        super().__init__(name,addr,emp_count)
        self.projects=projects

    def display_projects(self):
        print("IT DEPARTMENT PROJECTS : ")
        for project in self.projects:
            print(f' - {project}')
    
class HrDepartment(Company):
    def __init__(self,name,addr,emp_count,hiringprocess):
        super().__init__(name,addr,emp_count)
        self.hiring_process=hiringprocess

    def display_hiring_process(self):
        print("HR HIRING PROCESS IS:")
        for round in self.hiring_process:
            print(f'-{round}')

it=ItDepartment("tech","marathahalli-630012",100,["spam detection","bank application","ecommerce site","project-4","project-5"])
hr=HrDepartment("tech","marathahalli-630012",100,["1.APPLICATION SHORTLIST","2.APTITUDE ROUND","3.COMMUNICATION ROUND",
"4.TECHNICAL ROUND","5.HR INTERVIEW","RECRUITING"])

it.company_details()
it.display_projects()

hr.company_details()
hr.display_hiring_process()
'''
# MULTI-LEVEL-INHERITANCE
'''
class Institute:
    def __init__(self,name,addr,trainers_count):
        self.institute=name
        self.address=addr
        self.faculty_count=trainers_count
    def show_details(self):
        print(f'INSTITUTE NAME = {self.institute}')
        print(f'INSTITUTE ADDRESS = {self.address}')
        print(f'FACULTY COUNT = {self.faculty_count}')
class Trainer(Institute):
    def __init__(self, name, addr, trainers_count,tname,tage,tid):
        self.t_name=tname
        self.t_age=tage
        self.t_id=tid
        super().__init__(name, addr, trainers_count)

    def show_details(self):
        super().show_details()
        print(f'NAME OF TRAINER IS {self.t_name}')
        print(f"TRAINER'S AGE IS {self.t_age}")
        print(f'TRAINER ID = {self.t_id}')
class Student(Trainer):
    def __init__(self,sname,sage,sid,smail,scontact,tname, tage, tid, name, addr, trainers_count):
        self.S_IDNO=sid
        self.S_NAME=sname
        self.S_AGE=sage
        self.S_MAIL_ID=smail
        self.CONTACT=scontact
        super().__init__(name, addr, trainers_count, tname, tage, tid)

    def show_details(self):
        super().show_details()
        print(f'STUDENT NAME = {self.S_NAME}')
        print(f'STUDENT ID = {self.S_IDNO}')
        print(f'STUDENT AGE = {self.S_AGE}')
        print(f'STUDENT EMAIL = {self.S_MAIL_ID}')
        print(f'STUDENT CONTACT IS {self.CONTACT}')
jsp=Institute("JSPYDERS","MARATHAHALLI",50)
ab=Student("ABISHK",21,123123,"abishk.akr@gmail.com",636362232,"SHV",30,333333,"JSPIDERS","MARATHAHALLI",50)
ab.show_details()
jsp.show_details()
'''


