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
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            raise ValueError('Amount exceeds balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance -= amount


# Test code for 10.3
if __name__ == "__main__":
    acct1 = Account("John Green", Decimal("50.00"))
    print("Initial balance:", acct1.balance)

    # Directly overriding the attribute (bypasses validation!)
    acct1.balance = Decimal("-1000.00")
    print("After direct assignment:", acct1.balance)