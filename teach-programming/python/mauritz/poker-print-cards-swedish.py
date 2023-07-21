suits = ["Hjärter", "Spader", "Ruter", "Klöver"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]
count = 0
for i in suits:
    for j in values:
        print(f"{j} i {i}")
        count += 1
print(f"Det finns {count} kort i en kortlek")

def is_flush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return True
    else:
        return False

def is_straight(hand):
    if hand[0][0] == hand[1][0] - 1 == hand[2][0] - 2 == hand[3][0] - 3 == hand[4][0] - 4:
        return True
    else:
        return False
    
def is_royal(hand):
    if hand[0][0] == 10 and hand[1][0] == 11 and hand[2][0] == 12 and hand[3][0] == 13 and hand[4][0] == 14:
        return True
    else:
        return False

def is_royal_flush(hand):
    if is_flush(hand) and is_straight(hand) and is_royal(hand):
        return True
    else:
        return False
