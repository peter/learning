import argparse
import random
from collections import defaultdict

def first(the_iterable, condition = lambda x: True):
    for i in the_iterable:
        if condition(i):
            return i

def get_winner(points, points_to_win):
  for player, player_points in points.items():
    if player_points >= points_to_win:
      return player

def other_player(config, player):
  for p in config['players']:
    if p != player:
      return p

def valid_choice(config, choice):
  return choice in config['choices']

def winning_choice(choice, other_choice):
  return (choice == 'sten' and other_choice == 'sax' or
    choice == 'sax' and other_choice == 'påse' or
    choice == 'påse' and other_choice == 'sten')

def update_points(config, points, choices):
  new_points = {}
  for player, choice in choices.items():
    other_choice = choices[other_player(config, player)]
    if winning_choice(choice, other_choice):
      new_points[player] = points[player] + 1
    else:
      new_points[player] = points[player]
    print(f"{player}: val={choice} poäng={new_points[player]}")
  return new_points

def update_state(state, updates):
  return {**state, **updates}

def random_strategy(config, state):
  return random.choice(config['choices'])

def imitate_strategy(config, state):
  if state['history']:
    return state['history'][-1]['spelare']
  else:
    return random_strategy(config, state)

def cycle_strategy(config, state):
  if state['history']:
    last_index = config['choices'].index(state['history'][-1]['dator'])
    new_index = (last_index + 1) % len(config['choices'])
    return config['choices'][new_index]
  else:
    return random_strategy(config, state)

def repeat_strategy(config, state):
  if state['history']:
    return state['history'][-1]['dator']
  else:
    return random_strategy(config, state)

def opposite_strategy(config, state):
  if state['history']:
    last_choice = state['history'][-1]['dator']
    return first(config['choices'], lambda c: winning_choice(c, last_choice))
  else:
    return random_strategy(config, state)

def repeat_cycle_strategy(config, state):
  if state['history']:
    if len(state['history']) >= 2 and state['history'][-2]['dator'] == state['history'][-1]['dator']:
      return cycle_strategy(config, state)
    else:
      return repeat_strategy(config, state)
  else:
    return random_strategy(config, state)

def computer_choice(config, state):
  return config['strategy'](config, state)

def parse_args(strategies):
  parser = argparse.ArgumentParser(description='Spela sten sax påse mot datorn')
  parser.add_argument('--strategy', choices=list(strategies))
  args = parser.parse_args()
  return args

def get_strategy(strategies, args):
  if 'strategy' in args:
    return strategies[args.strategy]
  else:
    return random.choice(strategies.values())

def game_loop(config):
  state = {
    'round': 1,
    'points': defaultdict(lambda: 0),
    'history': []
  }
  while not get_winner(state['points'], config['points_to_win']):
    print(f'\nOmgång {state["round"]}')
    choices = {
      'spelare': input("sten sax påse? "),
      'dator': computer_choice(config, state)
    }
    if not valid_choice(config, choices['spelare']):
      valid_choices = ", ".join(config['choices'])
      print(f'Ogiltigt val... Du måste välja ett av {valid_choices}')
      continue
    state = update_state(state, {
      'round': (state['round'] + 1),
      'points': update_points(config, state['points'], choices),
      'history': (state['history'] + [choices])
    })
  return state

def print_winner(config, state):
  if get_winner(state['points'], config['points_to_win']) == 'spelare':
    print('\nDu vann!!')
  else:
    print('\nDatorn vann...')

def main():
  strategies = {
    'random': random_strategy,
    'imitate': imitate_strategy,
    'cycle': cycle_strategy,
    'repeat': repeat_strategy,
    'opposite': opposite_strategy,
    'repeat_cycle': repeat_cycle_strategy
  }
  args = parse_args(strategies)
  config = {
    'players': ['spelare', 'dator'],
    'choices': ["sten", "sax", "påse"],
    'points_to_win': 3,
    'strategy': get_strategy(strategies, args)
  }
  state = game_loop(config)
  print_winner(config, state)

if __name__ == '__main__':
  main()
