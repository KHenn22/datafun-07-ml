from time_10_4 import Time

print("=== Creating a Time object ===")
wake_up = Time(hour=6, minute=30)
print("Initial:", wake_up)

print("\n=== Changing attributes ===")
wake_up.hour = 7
wake_up.minute = 45
print("After change:", wake_up)

print("\n=== Using set_time method ===")
wake_up.set_time(hour=8, minute=15, second=30)
print("After set_time:", wake_up)

print("\n=== Invalid values (should raise ValueError) ===")
try:
    wake_up.hour = 100
except ValueError as e:
    print("Error:", e)

try:
    wake_up.minute = 75
except ValueError as e:
    print("Error:", e)

try:
    wake_up.second = -5
except ValueError as e:
    print("Error:", e)