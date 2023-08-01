from random import randint

CHOICES = ["sten", "sax", "påse"]

def get_input():
    answer = input("sten sax påse? ")
    if not answer in CHOICES:
        print("Du måste välja en av sten, sax, eller påse")
        return get_input()
    return answer

def is_draw(player, computer):
    return player == computer

def player_wins(player, computer):
    return player == "sten" and computer == "sax" or \
        player == "sax" and computer == "påse" or \
        player == "påse" and computer == "sten"

while True:
    player = get_input()
    computer = CHOICES[randint(0, 2)]
    print(f"användarens val: {player}")
    print(f"datorns val: {computer}")
    if is_draw(player, computer):
        print("Oavgjort")
    elif player_wins(player, computer):
        print("Du vann!")
    else:
        print("Du förlorade!")
