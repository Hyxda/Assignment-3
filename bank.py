# Define Account Class
class Account:
    def __init__(self, account_num, interest, balance = 0):
        self.account_num = account_num
        self.interest = interest
        self.balance = balance

    def check_balance(self):
        return self.balance
    
    def deposit(self, deposit):
        self.balance += deposit
    
    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
        else:
            print("Insufficient Balance\n")