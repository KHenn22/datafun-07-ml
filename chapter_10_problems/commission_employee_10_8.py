from decimal import Decimal

class CommissionEmployee:
    """CommissionEmployee base class."""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales   # validate via property
        self.commission_rate = commission_rate  # validate via property

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError("Gross sales must be >= 0")
        self._gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError("Commission rate must be > 0 and < 1")
        self._commission_rate = rate

    def earnings(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return (f"CommissionEmployee: {self.first_name} {self.last_name}\n"
                f"social security number: {self.ssn}\n"
                f"gross sales: {self.gross_sales:.2f}\n"
                f"commission rate: {self.commission_rate:.2f}")

# ------------------- TEST SECTION -------------------
if __name__ == "__main__":
    c = CommissionEmployee('Sue', 'Jones', '333-33-3333',
                           Decimal('10000.00'), Decimal('0.06'))
    print(c)
    print(f"Earnings: {c.earnings():.2f}")