from random import random

ALTERNATIV = ['sten', 'sax', 'påse']
ANTAL_SPEL = 5

def play():
  dator_val = ALTERNATIV[round(random()*(len(ALTERNATIV) - 1))]
  val = input('Sten, sax, eller påse?')
  if val == 'sten' and dator_val == 'sax' or val == 'sax' and dator_val == 'påse' or val == 'påse' and dator_val == 'sten':
    print(f'1 poäng (val={val} dator_val={dator_val})')
    return 1
  elif val == dator_val:
    print(f'0 poäng (val={val} dator_val={dator_val})')
    return 0
  else:
    print(f'-1 poäng (val={val} dator_val={dator_val})')
    return -1

points = 0
for i in range(0, ANTAL_SPEL):
  points += play()
print(f'Du fick {points} poäng!')
