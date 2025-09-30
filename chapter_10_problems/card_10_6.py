# card_10_6.py
"""Card class that represents a playing card."""

class Card:
    """Represents a playing card with a face and suit."""

    # Class attributes
    FACES = ['Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card’s face."""
        return self._face

    @property
    def suit(self):
        """Return the Card’s suit."""
        return self._suit

    @property
    def image_name(self):
        """Return the Card’s image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return a user-friendly string for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format_spec):
        """Format a card using str()."""
        return f'{str(self):{format_spec}}'