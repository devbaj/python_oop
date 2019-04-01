class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

zeroTwo = User("Zero Two", "02@franxx.com")
mai = User("Sakurajima Mai", "mai@idol.org")
chika = User("Fujiwara Chika", "fujiwara-shoki@shuchiin.edu")

zeroTwo.make_deposit(200)
zeroTwo.make_deposit(50)
zeroTwo.make_deposit(420)
zeroTwo.make_withdrawal(78)
print(f"User: {zeroTwo.name}, Balance: ${zeroTwo.account_balance}")

mai.make_deposit(82)
mai.make_deposit(53)
mai.make_withdrawal(22)
mai.make_withdrawal(37)
print(f"User: {mai.name}, Balance: ${mai.account_balance}")

chika.make_deposit(639)
chika.make_withdrawal(73)
chika.make_withdrawal(48)
chika.make_withdrawal(26)
print(f"User: {chika.name}, Balance: ${chika.account_balance}")

zeroTwo.transfer_money(chika, 150)
print(f"User: {zeroTwo.name}, Balance: ${zeroTwo.account_balance}")
print(f"User: {chika.name}, Balance: ${chika.account_balance}")