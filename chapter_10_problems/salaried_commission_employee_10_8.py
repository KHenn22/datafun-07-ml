from decimal import Decimal
from commission_employee_10_8 import CommissionEmployee

class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who gets a salary plus commission based on gross sales."""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)
        self.base_salary = base_salary  # validate via property

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, salary):
        if salary < Decimal('0.00'):
            raise ValueError("Base salary must be >= 0")
        self._base_salary = salary

    def earnings(self):
        return super().earnings() + self.base_salary

    def __repr__(self):
        return (f"Salaried {super().__repr__()}\n"
                f"base salary: {self.base_salary:.2f}")

# ------------------- TEST SECTION -------------------
if __name__ == "__main__":
    s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
                                   Decimal('5000.00'), Decimal('0.04'), Decimal('300.00'))
    print(s)
    print(f"Earnings: {s.earnings():.2f}")
    