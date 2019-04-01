class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self

acct1 = BankAccount(0.005, 100)
acct2 = BankAccount(0.013, 650)

acct1.deposit(50).deposit(28).deposit(640).withdraw(180).yield_interest().display_account_info()

acct2.deposit(930).deposit(430).withdraw(80).withdraw(275).withdraw(59).withdraw(397).yield_interest().display_account_info()