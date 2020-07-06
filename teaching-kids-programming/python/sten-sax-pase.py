import argparse
import random
from collections import defaultdict

CONFIG = {
  'players': ['spelare', 'dator'],
  'choices': ["sten", "sax", "påse"],
  'points_to_win': 3
}

STATE = {
  'round': 0,
  'points': defaultdict(lambda: 0),
  'history': []
}

def get_winner(points, points_to_win):
  for player, player_points in points.items():
    if player_points >= points_to_win:
      return player

def other_player(player):
  for p in CONFIG['players']:
    if p != player:
      return p

def valid_choice(choice):
  return choice in CONFIG['choices']

def winning_choice(choice, other_choice):
  return (choice == 'sten' and other_choice == 'sax' or
    choice == 'sax' and other_choice == 'påse' or
    choice == 'påse' and other_choice == 'sten')

def update_points(choices):
    for player, choice in choices.items():
      other_choice = choices[other_player(player)]
      if winning_choice(choice, other_choice):
        STATE['points'][player] += 1
      print(f"{player}: val={choice} poäng={STATE['points'][player]}")

def random_strategy():
  return random.choice(CONFIG['choices'])

def cycle_strategy():
  if STATE['history']:
    last_index = CONFIG['choices'].index(STATE['history'][-1]['dator'])
    new_index = (last_index + 1) % len(CONFIG['choices'])
    print(f'last_index={last_index} new_index={new_index}')
    return CONFIG['choices'][new_index]
  else:
    return random_strategy()

def imitate_strategy():
  if STATE['history']:
    return STATE['history'][-1]['spelare']
  else:
    return random_strategy()

def repeat_strategy():
  if STATE['history']:
    return STATE['history'][-1]['dator']
  else:
    return random_strategy()

STRATEGIES = {
  'random': random_strategy,
  'cycle': cycle_strategy,
  'imitate': imitate_strategy,
  'repeat': repeat_strategy
}

def computer_choice():
  return STRATEGIES[CONFIG['strategy']]()

def parse_args():
  parser = argparse.ArgumentParser(description='Spela sten sax påse mot datorn')
  parser.add_argument('--strategy', choices=list(STRATEGIES))
  args = parser.parse_args()
  return args

def set_strategy(args):
  if 'strategy' in args:
    CONFIG['strategy'] = args.strategy
  else:
    CONFIG['strategy'] = random.choice(list(STRATEGIES))

def game_loop():
  while not get_winner(STATE['points'], CONFIG['points_to_win']):
    STATE['round'] += 1
    print(f'\nOmgång {STATE["round"]}')
    choices = {
      'spelare': input("sten sax påse? "),
      'dator': computer_choice()
    }
    if not valid_choice(choices['spelare']):
      valid_choices = ", ".join(CONFIG['choices'])
      print(f'Ogiltigt val... Du måste välja ett av {valid_choices}')
      continue
    update_points(choices)
    STATE['history'].append(choices)

def print_winner():
  if get_winner(STATE['points'], CONFIG['points_to_win']) == 'spelare':
    print('\nDu vann!!')
  else:
    print('\nDatorn vann...')

def main():
  args = parse_args()
  set_strategy(args)
  game_loop()
  print_winner()

if __name__ == '__main__':
  main()
