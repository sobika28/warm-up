
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.owner}'s account balance: Rs. {self.balance:.2f}"


# Short test section
account = BankAccount("Sobika", 1000)

assert account.balance == 1000
assert account.deposit(500) == 1500
assert account.withdraw(200) == 1300

try:
    account.withdraw(5000)
except ValueError:
    pass
else:
    raise AssertionError("Overdraft should have been rejected.")

print(account)
print("All BankAccount tests passed!")
