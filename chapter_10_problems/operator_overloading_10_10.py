# operator_overloading_10_10.py
"""Complex number class with operator overloading for + and +=."""

class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        """Initialize Complex(real, imaginary)."""
        self.real = float(real)
        self.imaginary = float(imaginary)

    # ----- operator overloading -----
    def __add__(self, right):
        """Return a new Complex that is the sum of self and right."""
        if not isinstance(right, Complex):
            return NotImplemented
        return Complex(self.real + right.real,
                       self.imaginary + right.imaginary)

    def __iadd__(self, right):
        """In-place addition: self += right."""
        if not isinstance(right, Complex):
            return NotImplemented
        self.real += right.real
        self.imaginary += right.imaginary
        return self

    def __radd__(self, left):
        """Support sum() and reversed addition."""
        if left == 0:  # sum() starts with 0
            return self
        if isinstance(left, Complex):
            return left + self
        return NotImplemented

    # ----- representation -----
    def __repr__(self):
        """Return a friendly representation like (a + bi)."""
        sign = '+' if self.imaginary >= 0 else '-'
        return f'({self.real} {sign} {abs(self.imaginary)}i)'