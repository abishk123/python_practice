'''class Bank():
    bank_name='SBI'
    bank_roi=6
    bank_branch='vayalpad'
    def __init__(self,cnam, cmob, cage, cacc, cbal):
        self.name=cnam
        self.mobile=cmob
        self.age=cage
        self.acc_no=cacc
        self.balance=cbal

    def withdraw(self):
        amount=int(input('enter withdrawl amount : '))
        if self.balance >= amount:
            self.balance -= amount
            print("WITHDRAWAL OF {amount} IS SUCCESSFUL")
        else:
            print("INSUFFICIENT FUNDS")
        print(f'CURRENT BALANCE IS {self.balance}')
    
    def deposit(self):
        amount=int(input('enter amount for deposit : '))
        self.balance += amount
        print(f'DEPOSIT OF {amount} IS SUCCESSFUL')


abhi=Bank('ABHISHEK',6303824473,21,6638823620,1250)

surya=Bank('SURYA', 7013332900, 25, 789987899, 45000)

abhi.withdraw()

abhi.deposit()
print(abhi.balance)







# accessing class variables using class
print(Bank.bank_name)
print(Bank.bank_roi)
print(Bank.bank_branch)

# accessing class variables using object
print(abhi.bank_name)
print(abhi.bank_roi)
print(abhi.bank_branch)

# modifying class variable using class
Bank.bank_branch='MADANAPALLI'

print(Bank.bank_branch)
print(abhi.bank_branch)

# modifying class variable using object
abhi.bank_name='INDIAN BANK'

print(Bank.bank_name)
print(abhi.bank_name)

'''
# EXERCISE-1
'''
class Bank:
    bank_name='INDIAN BANK'
    bank_ifsc= 'IDIB000V030'
    bank_roi=6
    def __init__(self,cnam, cage, cacc, cpin,cbal=10000):
        self.c_name=cnam
        self.c_age=cage
        self.c_account=cacc
        self.c_pin=cpin
        self.c_balance=cbal

    def withdraw(self):
        pin=int(input('pin:'))
        if pin==self.c_pin:
            amount=int(input('enter withdrawl amount : '))
            if self.c_balance >= amount:
                self.c_balance -= amount
                print(f"WITHDRAWAL OF {amount} IS SUCCESSFUL")
            else:
                print("INSUFFICIENT FUNDS")
            print(f'CURRENT BALANCE IS {self.c_balance}')
        else:
            print('Incorrect Pin:Enter Valid Pin')
    
    def deposit(self):
        amount=int(input('enter amount for deposit : '))
        self.c_balance += amount
        print(f'DEPOSIT OF rs.{amount} IS SUCCESSFUL TO {self.c_account}')

    def show_details(self):
        print(f'NAME : {self.c_name}')
        print(f'AGE : {self.c_age}')
        print(f'ACCOUNT : {self.c_account}')
        print('CPIN : ******')
        print(f'BALANCE : {self.c_balance}')

    @classmethod
    def bank_details(cls):
        print(f'BANK NAME : {cls.bank_name}')
        print(f'BANK IFSC : {cls.bank_ifsc}')
        print(f'BANK ROI : {cls.bank_roi}')
    
    @classmethod
    def modify_roi(cls):
        new_roi=int(input('roi:'))
        cls.bank_roi=new_roi
    

ab=Bank('S ABHISHEK KUMAR REDDY', 21, 6638823620, 1021, 1500)
su=Bank('S SURYA PRAKASH REDDY', 25, 7013332900, 625625)
da=Bank('S RAMANA REDDY', 43, 6300698455, 9010, 45000)

ab.show_details()
su.show_details()
da.show_details()

ab.withdraw()
ab.deposit()

ab.show_details()

Bank.bank_details()

Bank.modify_roi()

Bank.bank_details()
'''

#EXERCISE-2

class School:
    school_name='JSPIDERS'
    school_loc='BENGALURU'
    principal_name='MR.HARSHAD'

    def __init__(self, student_name, student_age, student_class):
        self.name=student_name
        self.age=student_age
        self.cource=student_class

    @classmethod
    def school_details(cls):
        print(f'SCHOOL NAME : {cls.school_name}')
        print(f'SCHOOL LOCATION : {cls.school_loc}')
        print(f'SCHOOL PRINCIPAL : {cls.principal_name}')

    def student_details(self):
        print(f'STUDENT NAME : {self.name}')
        print(f'STUDENT AGE : {self.age}')
        print(f'STUDENT COURSE : {self.cource}')

    @classmethod
    def change_location(cls):
        cls.school_loc=input('loc : ')
    
    def update_cource(self):
        self.cource=input('cource : ')

ni=School('NITISH KUMAR', 22, 'PYTHON FS')
mu=School('MURALI', 21, 'PYTHON FULL STACK')
de=School('DEVANDRA', 23, 'MERN')
'''
ni.student_details()
mu.student_details()
de.student_details()

School.school_details()
de.school_details()
de.student_details()'''
School.change_location()
School.school_details()
de.update_cource()
de.student_details()


