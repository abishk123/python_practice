class Bank_V1:
    bank_name='SBI'
    bank_roi=7
    bank_branch='MYSORE'
    def __init__(self,cnam,cage,cacc,cbal):
        self.c_name=cnam
        self.c_age=cage
        self.c_account=cacc
        self.c_balance=cbal

    def customer_details(self):
        print(f'NAME OF THE CUSTOMER IS {self.c_name}')
        print(f'AGE OF THE CUSTOMER IS {self.c_age}')
        print(f'ACCOUNT NO OF THE CUSTOMER IS {self.c_account}')
        print(f'BALANCE OF THE CUSTOMER IS {self.c_balance}')

    @classmethod
    def bank_details(cls):
        print(f'NAME OF THE BANK IS {cls.bank_name}')
        print(f'ROI OF THE BANK IS {cls.bank_roi}')
        print(f'BRANCH OF THE BANK IS {cls.bank_branch}')

    def withdraw(self):
        amount=self.get_int_value()
        if amount<=self.c_balance:
            self.c_balance-=amount
            print(f'withdraw of amt {amount} is successful \ncurrent balance after withdraw is amt {self.c_balance}')
        else:
            print('INSUFFICIENT FUNDS')
        
    def deposit(self):
        amount=self.get_int_value()
        self.c_balance+=amount
        print('DEPOSIT IF SUCCESSFUL')

    @staticmethod
    def get_int_value():
        value=int(input('int value: '))
        return value

    



class Bank_V2(Bank_V1):
    bank_branch='BENGALURU'
    bank_mobile=8888888888

    def __init__(self,cnam,cage,cacc,cbal,cpin,caad):
        self.c_name=cnam
        self.c_age=cage
        self.c_account=cacc
        self.c_balance=cbal
        self.c_pin=cpin
        self.c_aadhar=caad

    def customer_details(self):
        print(f'NAME OF THE CUSTOMER IS {self.c_name}')
        print(f'AGE OF THE CUSTOMER IS {self.c_age}')
        print(f'ACCOUNT NO OF THE CUSTOMER IS {self.c_account}')
        print(f'BALANCE OF THE CUSTOMER IS {self.c_balance}')
        print(f'AADHAR NO.. OF THE CUSTOMER IS {self.c_aadhar}')

    @classmethod
    def bank_details(cls):
        print(f'NAME OF THE BANK IS {cls.bank_name}')
        print(f'ROI OF THE BANK IS {cls.bank_roi}')
        print(f'BRANCH OF THE BANK IS {cls.bank_branch}')
        print(f'MOBILE NO.OF BANK IS {cls.bank_mobile}')

    def withdraw(self):
        pin=self.get_int_value()
        if pin==self.c_pin:
            amount=self.get_int_value()
            if amount<=self.c_balance:
                self.c_balance-=amount
                print(f'withdraw of amt {amount} is successful \ncurrent balance after withdraw is amt {self.c_balance}')

            else:
                print('INSUFFICIENT FUNDS')
        else:
            print('INCORRECT PIN,PLEASE ENTER VALID PIN')
    
    @classmethod
    def change_roi(cls):
        cls.roi=cls.get_int_value()

    def change_pin(self):
        self.c_pin=self.get_int_value()


jay=Bank_V1('JAY',22,12122,10000)
mur=Bank_V2('MURALI',56,25825869,1016,6969,789789555252)
jay.withdraw()
jay.bank_details()
jay.customer_details()
print("")
mur.withdraw()
mur.bank_details()
mur.customer_details()