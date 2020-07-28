class Account:
    minbal = 10000

    @staticmethod
    def get_minbal():
        return Account.minbal

    def __init__(self, acno, customer, balance=0):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= Account.minbal:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance!")

    @property
    def current_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno} - {self.customer} - {self.balance}"


a1 = Account(1, "Scott", 100000)
a1.withdraw(50000)
print(a1)
print(a1.current_balance)

