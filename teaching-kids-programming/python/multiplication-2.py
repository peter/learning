from random import randint
import re
import time

N_MULTIPLICATIONS = 5
DIFFICULTY_RANGE = 4
MAX_DIFFICULTY = 5

def get_numbers(difficulty):
  result = []
  for n in range(1, N_MULTIPLICATIONS + 1):
    # for range 4: 2-6, 6-10, 10-14, 14-18, 18-22
    min = 2 + (difficulty - 1) * DIFFICULTY_RANGE
    max = min + DIFFICULTY_RANGE
    a = randint(min, max)
    b = randint(min, max)
    result.append([n, a, b])
  return result

def print_number_area(a, b):
  for _ in range(0, a):
    print('*' * b)

def ask_difficulty():
  answer = input(f'Välj svårighetsgrad (1-{MAX_DIFFICULTY})? ')
  if answer.isdigit() and int(answer) >= 1 and int(answer) <= MAX_DIFFICULTY:
    return int(answer)
  else:
    difficulty = randint(1, 5)
    print(f'Jag väljer svårighetsgrad {difficulty} åt dig')
    return difficulty

def ask_multiplication(n, a, b):
  print_number_area(a, b)
  if a > 10:
    # a * b
    print(f'tips: 10 * {b} + {a - 10} * {b}')
  elif b > 10:
    print(f'tips: {a} * 10 + {a} * {b - 10})')
  answer = int(input(f"{n}. Hur mycket är {a} * {b}? "))
  if answer == a * b:
    print("Rätt!!!")
    return 1
  else:
    print(f"Fel, kom igen nu!!! Rätt svar är {a * b}")
    return 0

def main():
  difficulty = ask_difficulty()
  correct_count = 0
  start_time = time.time()
  for [n, a, b] in get_numbers(difficulty):
    correct_count += ask_multiplication(n, a, b)
  elapsed = time.time() - start_time
  if correct_count == N_MULTIPLICATIONS:
    print('\nAlla rätt, du är grym!')
    print(f'Din genomsnittliga svarstid per fråga: {round(elapsed/N_MULTIPLICATIONS)} sekunder')
    if (difficulty < MAX_DIFFICULTY):
      print(f'Testa svårighetsgrad {difficulty + 1} nästa gång! Klarar du den!?')
  else:
    print(f'Du hade {correct_count} rätt av {N_MULTIPLICATIONS}. Testa igen! Träning ger färdighet')

if __name__ == '__main__':
    main()
