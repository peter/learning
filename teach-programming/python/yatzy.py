from collections import defaultdict
import re
from random import randint

top_choices = [
  'ettor',
  'tvåor',
  'treor',
  'fyror',
  'femmor',
  'sexor',
]
bottom_choices = [
  '1 par',
  '2 par',
  'tretal',
  'fyrtal',
  'liten straight',
  'stor straight',
  'kåk',
  'chans',
  'yatzy',
]

def get_players():
  result = []
  names_string = input('Spelares förnamn? ')
  names = [name for name in re.compile(',|\s').split(names_string) if name]
  for name in names:
    result.append({'name': name, 'points': defaultdict(lambda: 0)})
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
  for choice in top_choices:
    line = [choice]
    for player in players:
      line.append(player['points'][choice])
    lines.append(line)

  for choice in bottom_choices:
    line = [choice]
    for player in players:
      line.append(player['points'][choice])
    lines.append(line)

  print()
  print_lines(lines)

def throw_dices(n_dices):
  return [randint(1, 6) for i in range(0, n_dices)]

players = get_players()
game_over = False
while not game_over:
  print_board(players)
  for player in players:
    keep = []
    throws = 0
    while throws < 3 and len(keep) < 5:
      dices = throw_dices(5 - len(keep))
      throws += 1
      print(f"{player['name']} försök {throws}: du slår tärningarna {dices}")
      keep_string = input("vilka tärningar vill du behålla? ")
      keep_indexes = [int(value) - 1 for value in re.findall(r'[12345]', keep_string)]
      keep = keep + [dices[index] for index in keep_indexes]
      print(f"du behåller följande tärningar: {keep}")
    choice = input('Var vill du lägga dina poäng?')