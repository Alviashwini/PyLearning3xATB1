# bank account bal
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


jp_chase = BankAccount()
print(jp_chase.bal)
jp_chase.deposit(101)
jp_chase.show_balance()
jp_chase.withdraw(99)
jp_chase.show_balance()





