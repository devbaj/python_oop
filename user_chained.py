class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

zeroTwo = User("Zero Two", "02@franxx.com")
mai = User("Sakurajima Mai", "mai@idol.org")
chika = User("Fujiwara Chika", "fujiwara-shoki@shuchiin.edu")

zeroTwo.make_deposit(200).make_deposit(50).make_deposit(420).make_withdrawal(78).display_user_balance()

mai.make_deposit(82).make_deposit(53).make_withdrawal(22).make_withdrawal(37).display_user_balance()

chika.make_deposit(639).make_withdrawal(73).make_withdrawal(48).make_withdrawal(26).display_user_balance()

zeroTwo.transfer_money(chika, 150).display_user_balance()
chika.display_user_balance()