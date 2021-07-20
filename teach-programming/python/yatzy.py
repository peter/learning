from collections import defaultdict
import re
from random import randint

def first(values):
  return values[0]

def counts(values):
  items = [{'value': v, 'count': values.count(v)} for v in set(values)]
  return sorted(items, key=lambda i: -i['value'])

def points_1_par(dices):
  items = [c for c in counts(dices) if c['count'] > 1]
  max_value = max([i['value'] for i in items])
  return max_value * 2

def points_2_par(dices):
  items = [c for c in counts(dices) if c['count'] > 1]
  return (items[0]['value'] + items[1]['value']) * 2

def points_tretal(dices):
  items = [c for c in counts(dices) if c['count'] > 2]
  return items[0]['value'] * 3

def points_fyrtal(dices):
  items = [c for c in counts(dices) if c['count'] > 3]
  return items[0]['value'] * 4

top_choices = [
  {
    'name': 'ettor',
    'valid': lambda dices: len([d for d in dices if d == 1]) > 0,
    'points': lambda dices: sum([d for d in dices if d == 1]),
  },
  {
    'name': 'tvåor',
    'valid': lambda dices: len([d for d in dices if d == 2]) > 0,
    'points': lambda dices: sum([d for d in dices if d == 2]),
  },
  {
    'name': 'treor',
    'valid': lambda dices: len([d for d in dices if d == 3]) > 0,
    'points': lambda dices: sum([d for d in dices if d == 3]),
  },
  {
    'name': 'fyror',
    'valid': lambda dices: len([d for d in dices if d == 4]) > 0,
    'points': lambda dices: sum([d for d in dices if d == 4]),
  },
  {
    'name': 'femmor',
    'valid': lambda dices: len([d for d in dices if d == 5]) > 0,
    'points': lambda dices: sum([d for d in dices if d == 5]),
  },
  {
    'name': 'sexor',
    'valid': lambda dices: len([d for d in dices if d == 6]) > 0,
    'points': lambda dices: sum([d for d in dices if d == 6]),
  },
]
bottom_choices = [
  {
    'name': '1 par',
    'valid': lambda dices: len([c for c in counts(dices) if c['count'] > 1]) > 0,
    'points': points_1_par,
  },
  {
    'name': '2 par',
    'valid': lambda dices: len([c for c in counts(dices) if c['count'] > 1]) > 1,
    'points': points_2_par,
  },
  {
    'name': 'tretal',
    'valid': lambda dices: len([c for c in counts(dices) if c['count'] > 2]) > 1,
    'points': points_tretal,
  },
  {
    'name': 'fyrtal',
    'valid': lambda dices: len([c for c in counts(dices) if c['count'] > 3]) > 1,
    'points': points_fyrtal,
  },
  {
    'name': 'liten straight',
    'valid': lambda dices: len(set(dices)) == len(dices) and sorted(dices)[0] == 1,
    'points': lambda dices: 1 + 2 + 3 + 4 + 5,
  },
  {
    'name': 'stor straight',
    'valid': lambda dices: len(set(dices)) == len(dices) and sorted(dices)[0] == 2,
    'points': lambda dices: 2 + 3 + 4 + 5 + 6,
  },
  {
    'name': 'kåk',
    'valid': lambda dices: len(set(dices)) == len(dices) and sorted(dices)[0] == 2,
    'points': lambda dices: 2 + 3 + 4 + 5 + 6,
  },
  {
    'name': 'chans',
    'valid': lambda dices: True,
    'points': lambda dices: sum(dices),
  },
  {
    'name': 'yatzy',
    'valid': lambda dices: len(set(dices)) == 1,
    'points': lambda dices: sum(dices),
  },
]
all_choices = top_choices + bottom_choices

def get_players():
  result = []
  names_string = input('Spelares förnamn? ')
  names = [name for name in re.compile(',|\s').split(names_string) if name]
  for name in names:
    result.append({'name': name, 'points': {}})
  return result

def print_lines(lines):
  column_lengths = []
  for column_index in range(0, len(lines[0])):
    max_length = max([len(str(line[column_index])) for line in lines])
    column_lengths.append(max_length)

  for line in lines:
    padded_line = []
    for column_index in range(0, len(line)):
      pad_length = column_lengths[column_index] - len(str(line[column_index]))
      padded_value = str(line[column_index]) + ' ' * pad_length
      padded_line.append(padded_value)
    print('| ' + ' | '.join(padded_line) + ' |')

def print_board(players):
  lines = []
  lines.append([''] + [player['name'] for player in players])
  for choice in [c['name'] for c in top_choices]:
    line = [choice]
    for player in players:
      line.append(player['points'].get(choice, ''))
    lines.append(line)

  for choice in [c['name'] for c in bottom_choices]:
    line = [choice]
    for player in players:
      line.append(player['points'].get(choice, ''))
    lines.append(line)

  print()
  print_lines(lines)

def throw_dices(n_dices):
  return [randint(1, 6) for i in range(0, n_dices)]

players = get_players()
game_over = False
while not game_over:
  for player in players:
    print_board(players)
    dices = []
    keep = []
    throws = 0
    while throws < 3 and len(keep) < 5:
      dices = throw_dices(5 - len(keep))
      throws += 1
      print(f"{player['name']} - försök {throws} - du slår tärningarna {dices}")
      keep_string = input("vilka tärningar vill du behålla? ")
      keep_indexes = [int(value) - 1 for value in re.findall(r'[12345]', keep_string)]
      keep = keep + [dices[index] for index in keep_indexes]
      print(f"du behåller följande tärningar: {keep}")
    keep = keep or dices
    valid_choice = None
    while not valid_choice:
      choice_input = input('Var vill du lägga dina poäng?')
      choice = next(c for c in all_choices if c['name'] == choice_input)
      if (not choice_input in player['points']) and choice and choice['valid'](keep):
        valid_choice = choice
        player['points'][valid_choice['name']] = choice['points'](keep)
  # TODO: check if game is over, i.e. if all choices are made
