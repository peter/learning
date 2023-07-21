from random import randint
from collections import Counter
import re

SUITS = ["Hjärter", "Spader", "Ruter", "Klöver"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]

def shuffle(cards):
    result = []
    while len(cards) > 0:
        index = randint(0, len(cards) - 1)
        result.append(cards.pop(index))
    return result

def get_suit(card):
    return card[0]

def get_value(card):
    return card[1]

def get_rank(value):
    return VALUES.index(value) + 2

def get_value_counts(hand):
    values = [get_value(card) for card in hand]
    return Counter(values).most_common()

def get_suit_counts(hand):
    suits = [get_suit(card) for card in hand]
    return Counter(suits).most_common()

def get_sorted_hand(hand):
    return sorted(hand, key=get_value)

def print_hand(hand):
    for index, card in enumerate(hand):
        print(index + 1, card[0], card[1])

def is_flush(hand):
   return len(set([card[0] for card in hand])) == 1

def is_consecutive(card1, card2):
    return VALUES.index(card1[1]) == (VALUES.index(card2[1]) - 1)

def is_straight(hand):
    for index, _ in enumerate(hand):
        if index > 0 and not is_consecutive(hand[index - 1], hand[index]):
            return False
    return True

def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)

def is_royal_straight_flush(hand):
    return is_straight_flush(hand) and hand[0][1] == '10'

def is_four_of_a_kind(hand):
    return get_value_counts(hand)[0][1] == 4

def is_three_of_a_kind(hand):
    return get_value_counts(hand)[0][1] >= 3

def is_full_house(hand):
    counts = get_value_counts(hand)
    return counts[0][1] == 3 and counts[1][1] == 2

def is_two_pair(hand):
    counts = get_value_counts(hand)
    return counts[0][1] == 2 and counts[1][1] == 2

def is_one_pair(hand):
    return get_value_counts(hand)[0][1] >= 2

def is_high_card(hand):
    return True

HAND_TYPES = [
    is_high_card,
    is_one_pair,
    is_two_pair,
    is_three_of_a_kind,
    is_straight,
    is_flush,
    is_full_house,
    is_four_of_a_kind,
    is_straight_flush,
    is_royal_straight_flush,
]

def get_hand_type(hand):
    sorted_hand = get_sorted_hand(hand)
    index = len(HAND_TYPES) - 1
    while index >= 0:
        type_fn = HAND_TYPES[index]
        if (type_fn(sorted_hand)):
            return index
        index -= 1

def get_hand_value_rank(hand):
    # NOTE: giving precedence to rank of cards that occur the most
    counts = sorted(get_value_counts(hand), reverse=True, key=lambda c: (c[1], get_rank(c[0])))
    return [get_rank(count[0]) for count in counts]

def get_hand_type_name(hand_type):
    name = HAND_TYPES[hand_type].__name__
    return re.sub(r'_', ' ', re.sub(r"^is_", '', name))

def get_hand_rank(hand):
    return [get_hand_type(hand), *get_hand_value_rank(hand)]

def get_computer_changes(hand):
    hand_type = get_hand_type(hand)
    # If straight or better then keep the hand without changes
    if hand_type > 3:
        return ()
    value_counts = get_value_counts(hand)
    # If four cards straight or flush then change the fifth card
    for change_index, _ in enumerate(hand):
        four_cards = [card for index, card in enumerate(hand) if index != change_index]
        if is_flush(four_cards) or is_straight(four_cards):
            return tuple([change_index])
    if value_counts[0][1] == 2 and value_counts[1][1] == 2:
        # If two pairs, then change the fifth card
        value_to_change = value_counts[2][0]
        index_to_change = [get_value(card) for card in hand].index(value_to_change)
        return tuple([index_to_change])
    elif value_counts[0][1] == 3:        
        # If three of a kind, then change two cards
        keep_value = value_counts[0][0]
        return tuple([hand.index(card) for card in hand if get_value(card) != keep_value])
    elif value_counts[0][1] == 2:
        # If only one pair, then change three cards
        keep_value = value_counts[0][0]
        return tuple([hand.index(card) for card in hand if get_value(card) != keep_value])
    else:
        # Else change all cards
        return tuple([index for index, _ in enumerate(hand)])

def is_winner(rank1, rank2):
    for index, r1 in enumerate(rank1):
        r2 = rank2[index]
        if r1 != r2:
            return r1 > r2
    return None

def play_game():
    # Create shuffled deck of cards        
    cards = []
    for suit in SUITS:
        for value in VALUES:
            cards.append([suit, value])
    cards = shuffle(cards)

    # Deal random hands from the deck
    player_hand = []
    computer_hand = []
    for i in range(5):
        player_hand.append(cards.pop())
        computer_hand.append(cards.pop())

    for _ in range(2):
        print("\n####### DINA KORT\n")
        print_hand(player_hand)

        hand_type = get_hand_type(player_hand)
        suggested_changes = ''.join([str(i + 1) for i in get_computer_changes(player_hand)])
        user_input = input(f"\nVilka kort vill du byta (du har: {get_hand_type_name(hand_type)}, använd siffror 1-5 utan mellanslag, enter om du inte vill byta, tex. {suggested_changes})? ")
        if (user_input != ''):
            indexes = [int(v) for v in [*user_input]]
            for index in indexes:
                player_hand[index - 1] = cards.pop()

        computer_changes = get_computer_changes(computer_hand)
        print(f'Datorn byter {len(computer_changes)} kort')
        for index in computer_changes:
            computer_hand[index] = cards.pop()

    print("\n####### DINA KORT\n")
    print_hand(player_hand)
    player_rank = get_hand_rank(player_hand)

    print("\n####### DATORNS KORT\n")
    print_hand(computer_hand)
    computer_rank = get_hand_rank(computer_hand)

    print('\nDitt resultat:', get_hand_type_name(player_rank[0]), player_rank)
    print('Datorns resultat:', get_hand_type_name(computer_rank[0]), computer_rank)

    player_wins = is_winner(player_rank, computer_rank)
    if player_wins == True:
        print('DU VANN!')
    elif player_wins == False:
        print('Datorn vann')
    else:
        print('Epic fail - ingen vinnare kunde avgöras (detta är mycket osannolikt)!')
    return player_wins

def main():
    n_games = 0
    n_wins = 0
    while True:
        n_games += 1
        player_win = play_game()
        if player_win:
            n_wins += 1
        print('\n!!!!!!!!!!!!!!!!!!')
        print(f'\nDu har vunnit {n_wins}/{n_games} matcher!')
        print('\n!!!!!!!!!!!!!!!!!!\n')

if __name__ == "__main__":
    main()
