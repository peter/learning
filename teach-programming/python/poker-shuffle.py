import random

suits = ["Hjärter", "Spader", "Ruter", "Klöver"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]
cards = []
for suit in suits:
    for value in values:
        cards.append([suit, value])

def shuffle_cards(cards):
    remaining = cards.copy()
    result = []
    while len(remaining) > 0:
        index = random.randint(0, len(remaining) - 1)
        result.append(remaining.pop(index))
    return result

cards = shuffle_cards(cards)

print(len(cards), cards)
