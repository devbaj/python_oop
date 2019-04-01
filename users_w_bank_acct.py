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

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.accounts = [BankAccount(0.02, 0), BankAccount(0.02, 0), BankAccount(0.02, 0)]
    def make_deposit(self, amount, acct):
        self.accounts[acct].balance += amount
        return self
    def make_withdrawal(self, amount, acct):
        self.accounts[acct].balance -= amount
        return self
    def display_user_balance(self, acct):
        print(f"User: {self.name}, Account #{acct}, Balance: ${round(self.accounts[acct].balance, 2)}")
        return self
    def transfer_money(self, fromAcct, other_user, toAcct, amount):
        self.accounts[fromAcct].balance -= amount
        other_user.accounts[toAcct].balance += amount
        return self

zeroTwo = User("Zero Two", "02@franxx.com")
mai = User("Sakurajima Mai", "mai@idol.org")
chika = User("Fujiwara Chika", "fujiwara-shoki@shuchiin.edu")

zeroTwo.make_deposit(200, 1).make_deposit(50, 2).make_deposit(420, 1).make_withdrawal(78, 0)
zeroTwo.accounts[0].yield_interest()
zeroTwo.accounts[1].yield_interest()
zeroTwo.accounts[2].yield_interest()
zeroTwo.display_user_balance(0)
zeroTwo.display_user_balance(1)
zeroTwo.display_user_balance(2)

mai.make_deposit(82, 1).make_deposit(53, 2).make_withdrawal(22, 2).make_withdrawal(37, 1)
mai.accounts[0].yield_interest()
mai.accounts[1].yield_interest()
mai.accounts[2].yield_interest()
mai.display_user_balance(0)
mai.display_user_balance(1)
mai.display_user_balance(2)

chika.make_deposit(639, 0).make_withdrawal(73, 0).make_withdrawal(48, 0).make_withdrawal(26, 0)
chika.accounts[0].yield_interest()
chika.accounts[1].yield_interest()
chika.accounts[2].yield_interest()
chika.display_user_balance(0)
chika.display_user_balance(1)
chika.display_user_balance(2)

zeroTwo.transfer_money(1, chika, 2, 150)
zeroTwo.display_user_balance(1)
chika.display_user_balance(2)