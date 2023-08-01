from random import randint

CHOICES = ["sten", "sax", "påse"]

def player_wins(choice, computer):
    return choice == "sten" and computer == "sax" or \
        choice == "sax" and computer == "påse" or \
        choice == "påse" and computer == "sten"

while True:
    choice  = input("sten,sax,påse? ")
    computer = CHOICES[randint(0,2)]
    print("Datorns val", computer)

    if choice == computer:
        print("Oavgjort GG")
    elif player_wins(choice, computer):
        print("Du vann!!! GG")
    else:
        print("Datorn vann. GG")
