# account_doc_test_10_14.py
"""Account class definition with doctest examples."""

from decimal import Decimal

class Account:
    """Account class for demonstrating doctest."""

    def __init__(self, name, balance):
        """Initialize an Account object.
        
        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.name
        'John Green'
        >>> account1.balance
        Decimal('50.00')

        The balance argument must be greater than or equal to 0.
        >>> account2 = Account('John Green', Decimal('-50.00'))
        Traceback (most recent call last):
        ...
        ValueError: Initial balance must be >= to 0.00
        """
        #if balance is less than 0.00, raise an exceptiomn
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')
        
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account.
        
        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.deposit(Decimal('25.00'))
        >>> account1.balance
        Decimal('75.00')

        The amount argument must be positive.
        >>> account1.deposit(Decimal('-25.00'))
        Traceback (most recent call last):
        ...
        ValueError: Amount must be positive.
        """
        #if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        
        self.balance += amount

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)