from operator_overloading_10_10 import Complex

c1 = Complex(2, 3)     # 2 + 3i
c2 = Complex(-5, 7)    # -5 + 7i

print("c1:", c1)
print("c2:", c2)

# + creates a new Complex
c3 = c1 + c2
print("c1 + c2:", c3)

# += modifies left operand, then returns it
c1 += c2
print("c1 after += c2:", c1)

# Works with sum()
total = sum([Complex(1, 1), Complex(2, -3), Complex(0.5, 0.5)])
print("sum:", total)