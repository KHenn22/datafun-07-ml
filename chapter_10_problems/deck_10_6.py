# deck_10_6.py
"""DeckOfCards class that represents a deck of 52 cards."""

import random
from card_10_6 import Card

class DeckOfCards:
    """Represents a deck of 52 playing cards."""

    NUMBER_OF_CARDS = 52

    def __init__(self):
        """Initialize deck of cards."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            face = Card.FACES[count % 13]
            suit = Card.SUITS[count // 13]
            self._deck.append(Card(face, suit))

    def shuffle(self):
        """Shuffle the deck."""
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        """Deal one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except IndexError:
            return None  # No more cards

    def __str__(self):
        """Return a string of the full deck in 4 columns."""
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{card:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        return s