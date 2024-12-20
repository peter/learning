from collections import defaultdict
import re
from random import randint

def first(values):
  return values[0]

def get(values, index, default_value=None):
  return values[index] if index < len(values) else default_value

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
    'valid': lambda dices: sorted(dices) == [1, 2, 3, 4, 5],
    'points': lambda dices: 15,
  },
  {
    'name': 'stor straight',
    'valid': lambda dices: sorted(dices) == [2, 3, 4, 5, 6],
    'points': lambda dices: 20,
  },
  {
    'name': 'kåk',
    'valid': lambda dices: len(set(dices)) == 2 and len([c for c in counts(dices) if c['count'] == 3]) > 0,
    'points': lambda dices: sum(dices),
  },
  {
    'name': 'chans',
    'valid': lambda dices: True,
    'points': lambda dices: sum(dices),
  },
  {
    'name': 'yatzy',
    'valid': lambda dices: len(set(dices)) == 1,
    'points': lambda dices: 50,
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

def top_sum(player):
  return sum([player['points'].get(c['name'], 0) for c in top_choices])

def top_bonus(player):
  return 50 if top_sum(player) >= 63 else 0

def bottom_sum(player):
  return sum([player['points'].get(c['name'], 0) for c in bottom_choices])

def total_sum(player):
  return top_sum(player) + top_bonus(player) + bottom_sum(player)

def print_board(players):
  lines = []
  lines.append([''] + [player['name'] for player in players])
  for choice in [c['name'] for c in top_choices]:
    line = [choice]
    for player in players:
      line.append(player['points'].get(choice, ''))
    lines.append(line)
  empty_line = [''] + ['' for _ in players]
  lines.append(empty_line)
  lines.append(['summa'] + [top_sum(player) for player in players])
  lines.append(['bonus'] + [top_bonus(player) for player in players])
  lines.append(empty_line)
  for choice in [c['name'] for c in bottom_choices]:
    line = [choice]
    for player in players:
      line.append(player['points'].get(choice, ''))
    lines.append(line)
  lines.append(empty_line)
  lines.append(['summa'] + [total_sum(player) for player in players])

  print()
  print_lines(lines)
  print()

def throw_dices(n_dices):
  return [randint(1, 6) for i in range(0, n_dices)]

def keep_dices(keep_values, dices):
  left = dices.copy()
  result = []
  for value in keep_values:
    if value in left:
      result.append(value)
      left.remove(value)
  return result

def throw_dices_three_times(player):
  dices = []
  keep = []
  throws = 0
  MAX_THROWS = 3
  while throws < MAX_THROWS and len(keep) < 5:
    dices = keep + throw_dices(5 - len(keep))
    throws += 1
    print(f"{player['name']} - kast {throws} - tärningar: {dices}")
    if throws < MAX_THROWS:
      keep_string = input("vilka tärningar vill du behålla (skriv a för alla)? ")
      if keep_string == 'a':
        keep = dices
      else:
        keep_values = [int(v) for v in re.findall(r'[12345]', keep_string)]
        keep = keep_dices(keep_values, dices)
        print(f"du behåller följande tärningar: {keep}")
  return dices

def choose_points(player, dices):
  valid_choice = False
  while not valid_choice:
    choice_input = input('Var vill du lägga dina poäng?')
    choice = get([c for c in all_choices if c['name'] == choice_input], 0)
    if not choice:
      print('Ogiltigt val')
    elif choice_input in player['points']:
      print('Du har redan gjort det valet')
    else:
      valid_choice = True
      player['points'][choice['name']] = choice['points'](dices) if choice['valid'](dices) else 0

players = get_players()
for round in range(1, 16):
  print(f"runda {round}")
  for player in players:
    print_board(players)
    dices = throw_dices_three_times(player)
    choose_points(player, dices)
print_board(players)
winner = first(sorted(players, key=total_sum))
print(f"Vinnare är {winner['name']} med {total_sum(winner)} poäng!")
