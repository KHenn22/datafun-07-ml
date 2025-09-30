#####10.2 CUSTOM CLASS ACCOUNT PROBLEM#####
from decimal import Decimal

class Account:
    def __init__(self, name, balance):
        """Initialize an Account object."""
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance += amount


# Test code
if __name__ == "__main__":
    acct1 = Account("Kevin", Decimal("10.2"))
    print("Initial:", acct1.name, acct1.balance)

    acct1.deposit(Decimal("5.5"))
    print("After deposit:", acct1.name, acct1.balance)