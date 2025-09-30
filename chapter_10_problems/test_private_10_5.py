from private_10_5 import PrivateClass

obj = PrivateClass()

# Access public attribute directly
print("Public data:", obj.public_data)   # works fine

# Try to access private attribute
try:
    print("Private data:", obj.__private_data)  # should fail
except AttributeError as e:
    print("Error accessing __private_data:", e)

# Access private attribute using name mangling
print("Private data (via mangling):", obj._PrivateClass__private_data)