class Bank_V1:
    bank_name='SBI'
    bank_roi=7
    bank_branch='HYDERABAD'
    def __init__(self,cnam,cacc,cbal,cpin):
        self.c_name=cnam
        self.c_account=cacc
        self.c_balance=cbal
        self.c_pin=cpin

    def customer_details(self):
        print(f'NAME OF THE CUSTOMER IS {self.c_name}')
        print(f'ACC NO OF THE CUSTOMER IS {self.c_account}')
        print(f'BALANCE OF THE CUSTOMER IS {self.c_balance}')
        print(f'PIN OF THE CUSTOMER IS {self.c_pin}')
    @classmethod
    def bank_details(cls):
        print(f'NAME OF THE BANK IS {cls.bank_name}')
        print(f'ROI OF THE BANK IS {cls.bank_roi}')
        print(f'BRANCH OF THE BANK IS {cls.bank_branch}')
    def withdraw(self):
        pin=int(input("enter cpin: "))
        if pin==self.c_pin:
            amount=int(input('enter amt to withdraw:'))
            if amount<=self.c_balance:
                self.c_balance-=amount
                print(f'withdraw of amt {amount} is successful \ncurrent balance after withdraw is amt {self.c_balance}')

            else:
                print('INSUFFICIENT FUNDS')
        else:
            print('INCORRECT PIN,PLEASE ENTER VALID PIN')
        
    def deposit(self):
        amount=int(input('enter amt to deposit: '))
        self.c_balance+=amount
        print('DEPOSIT IF SUCCESSFUL')



class Bank_V2(Bank_V1):
    bank_branch='BENGALURU'
    bank_mobile=8888888888
    
    @staticmethod
    def get_int_value():
        value=int(input('int value: '))
        return value
    
    @classmethod
    def change_roi(cls):
        cls.roi=cls.get_int_value()

    @classmethod
    def bank_details(cls):
        print(f'NAME OF THE BANK IS {cls.bank_name}')
        print(f'ROI OF THE BANK IS {cls.bank_roi}')
        print(f'BRANCH OF THE BANK IS {cls.bank_branch}')
        print(f'MOBILE NO.OF BANK IS {cls.bank_mobile}')

    def change_pin(self):
        self.c_pin=self.get_int_value()

nitish=Bank_V1('NITISH', 12312312,45000,1000)
abhi=Bank_V2('ABHISHEK',6638823620,1300,1021)
print()
nitish.customer_details()
print()
abhi.customer_details()
print()
nitish.withdraw()
print()
abhi.bank_details()
print()
nitish.bank_details()


