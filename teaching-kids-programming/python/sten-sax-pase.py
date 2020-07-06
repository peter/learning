import random
from collections import defaultdict

CONFIG = {
  'choices': ["sten", "sax", "påse"],
  'points_to_win': 3
}

STATE = {
  'points': defaultdict(lambda: 0)
}

def get_winner(points, points_to_win):
  for player, player_points in points.items():
    if player_points >= points_to_win:
      return player

def other_player(player):
  return 'computer' if player == 'player' else 'player'

def valid_choice(choice):
  return choice in ['sten', 'sax', 'påse']

def winning_choice(choice, other_choice):
  return (choice == 'sten' and other_choice == 'sax' or
    choice == 'sax' and other_choice == 'påse' or
    choice == 'påse' and other_choice == 'sten')

def game_loop():
  while not get_winner(STATE['points'], CONFIG['points_to_win']):
    choices = {
      'player': input("\nsten sax påse? "),
      'computer': random.choice(CONFIG['choices'])
    }
    if not valid_choice(choices['player']):
      print('Ogiltigt val...')
      continue
    for player, choice in choices.items():
      other_choice = choices[other_player(player)]
      if winning_choice(choice, other_choice):
        STATE['points'][player] += 1
    print(f"användarens val: {choices['player']}, poäng: {STATE['points']['player']}")
    print(f"datorns val: {choices['computer']}, poäng: {STATE['points']['computer']}")

def print_winner():
  if get_winner(STATE['points'], CONFIG['points_to_win']) == 'player':
    print('\nDu vann!!')
  else:
    print('\nDatorn vann...')

def main():
  game_loop()
  print_winner()

if __name__ == '__main__':
  main()
