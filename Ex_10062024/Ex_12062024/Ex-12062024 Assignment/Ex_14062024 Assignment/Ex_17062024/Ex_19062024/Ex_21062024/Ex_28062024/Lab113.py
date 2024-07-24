# vlab 112 will fix the problem with encapsulation
class BankAccount:

    def __init__(self):
        self.bal = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("your balance is  ", self.balance)

        
