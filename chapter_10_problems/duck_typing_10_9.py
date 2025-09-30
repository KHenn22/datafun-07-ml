# duck_typing_10_9.py
from decimal import Decimal
from commission_employee_10_8 import CommissionEmployee
from salaried_commission_employee_10_8 import SalariedCommissionEmployee

class WellPaidDuck:
    def __repr__(self):
        return "I am a well-paid duck" 
    def earnings(self):
        return Decimal("1000000.00")

# Create objects
c = CommissionEmployee("Sue", "Jones", "333-33-3333",
                       Decimal("10000.00"), Decimal("0.06"))

s = SalariedCommissionEmployee("Bob", "Lewis", "444-44-4444",
                               Decimal("5000.00"), Decimal("0.04"), Decimal("300.00"))

d = WellPaidDuck()

# Put them all in one list
employees = [c, s, d]

# Loop through employees and call methods
for employee in employees:
    print(employee)
    print(f"Employee earnings: {employee.earnings():,.2f}\n")