from random import randint


class Bank:
    def __init__(self): #Non parameterize constructor
        self.account = randint(10000,1000001)
        self.name = input("Enter you full name : ")
        self.balance = 0
        self.phone = randint(99999999,100000000000)

    def show_balance(self) -> None:
        print("My account balance is {}".format(self.balance))

    def deposit(self)->None:
        amount = int(input("enter the deposit amount : "))
        self.balance += amount

    def withdraw(self):  
        amount = int(input("enter the deposit amount : "))
        if amount > self.balance:
            print(f"Insufficient balance : {self.balance}")
        else :
            self.balance-= amount


    
    def get_info(self):
        return f"Hello my name is {self.name} and My account no is {self.account}. The amount in my account is {self.balance}.and I can withdraw amount using my phone no {self.phone}"

Banks = []   
while True:
    print("1. create Bank account")
    print("2. Show all Bank details")
    print("3. enter amount to deposit")
    print("3. exit")
    choice = int(input("enter the choice"))

    if choice == 1 :
        obj = Bank()
        Banks.append(obj)
    elif choice == 2 :
        if len(Banks)==0:
            print("no account is created yet")
        else:
            for bank in Banks:
                print(bank.get_info())

    elif choice == 3:
        account = int(input("enter the account no. to deposit : "))
    
        for bank in Banks:
            if bank.account == account:
                bank.deposit()

    elif choice == 4:
        account = int(input("enter the account no. to deposit : "))
    
        for bank in Banks:
            if bank.account == account:
                bank.withdraw()
                break

    elif choice == 5:
        break

    else:
        print("invalid choice")
    


