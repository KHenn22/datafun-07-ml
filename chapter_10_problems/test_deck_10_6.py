from deck_10_6 import DeckOfCards

deck = DeckOfCards()

print("=== Initial Deck ===")
print(deck)

print("\n=== Shuffle Deck ===")
deck.shuffle()
print(deck)

print("\n=== Deal a few cards ===")
print("Dealt:", deck.deal_card())
print("Dealt:", deck.deal_card())

print("\n=== Deal until empty ===")
while True:
    card = deck.deal_card()
    if card is None:
        break
    print("Dealt:", card)