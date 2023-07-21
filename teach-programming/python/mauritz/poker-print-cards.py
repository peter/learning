# List with all the suites in a deck of cards
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

# List with all the values in a deck of cards
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Print all the cards in a deck of cards
for suit in suits:
    for value in values:
        print(f"{value} of {suit}")

# Calculate value of hand in poker
# def calculate_value(hand):
#     value = 0
#     for card in hand:
#         if card == "Jack" or card == "Queen" or card == "King":
#             value += 10
#         elif card == "Ace":
#             value += 11
#         else:
#             value += int(card)
#     return value
