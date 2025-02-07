
class BankAccount():
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} credited in your account. Current balance is {self.balance}")
        else:
            print("Enter a valid amount")
            
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} debited from your account. Current balance is {self.balance}")
            
        else:
            print("Insufficient funds")
            
    def balancecheck(self):
        print(f"Bank balance is {self.balance}")
            
            
acc=BankAccount("Anjana Jayapal",50000)
acc.deposit(6000)
acc.deposit(0)
acc.withdraw(30000)
acc.withdraw(100000)
acc.balancecheck()

        
        
        
        
# OUTPUT
'''
6000 credited in your account. Current balance is 56000
Enter a valid amount
30000 debited from your account. Current balance is 26000
Insufficient funds
Bank balance is 26000
'''