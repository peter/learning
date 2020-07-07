# From: https://www.youtube.com/watch?v=fB4Yp72ngR4
import random

h1 = [" _________",
 " | |",
 " | 0",
 " | ",
 " | ",
 " | ",
 " | ",
 " | ",
 " ___|___ "]

h2 = [" _________",
 " | |",
 " | 0",
 " | |",
 " | |",
 " | ",
 " | ",
 " | ",
 " ___|___ "]

h3 = [" _________",
 " |  |",
 " |  0",
 " | \|",
 " |  |",
 " | ",
 " | ",
 " | ",
 " ___|___ "]

h4 = [" _________",
 " |  |",
 " |  0",
 " | \|/",
 " |  |",
 " | ",
 " | ",
 " | ",
 " ___|___ "]

h5 = [" _________",
 " |  |",
 " |  0",
 " | \|/",
 " |  |",
 " | / ",
 " | ",
 " | ",
 " ___|___ "]

h6 = [" _________",
 " |  |",
 " |  0",
 " | \|/",
 " |  |",
 " | / \ ",
 " | ",
 " | ",
 " ___|___ "]

hangmans = [h1,h2,h3,h4,h5,h6]

ordlista = {
  'frukt': [
    "äpple",
    "avokado",
    "banan",
    "björnbär",
    "blåbär",
    "svarta vinbär",
    "körsbär",
    "klementin",
    "kokosnöt",
    "tranbär",
    "röda vinbär",
    "fikon",
    "grapefrukt",
    "vindruva",
    "kiwi",
    "citron",
    "lime",
    "mandarin",
    "mango",
    "nektarin",
    "apelsin",
    "passionsfrukt",
    "persika",
    "päron",
    "ananas",
    "plommon",
    "hallon",
    "satsuma",
    "jordgubbe",
    "vattenmelon"
  ],
  'stad': [
    'umeå',
    'stockholm',
    'boden',
    'linköping'
  ]
}

def print_word(word_type, word, guesses):
  available = guesses.copy()
  result = []
  for c in word:
    if c == ' ':
      result.append(' ')
    elif c in available:
      result.append(c)
      available.remove(c)
    else:
      result.append('_')
  print(f'{word_type} ({len(result)} bokstäver): {"".join(result)}')

def check_guesses(word, guesses):
  available = [w for w in word if w != ' ']
  mistakes_count = 0
  for guess in guesses:
    if guess in available:
      available.remove(guess)
    else:
      mistakes_count += 1
  available_count = len(available)
  return mistakes_count, available_count

def game_result(word, guesses):
  mistakes_count, available_count = check_guesses(word, guesses)
  if mistakes_count > len(hangmans):
    return 'failure'
  elif available_count == 0:
    return 'success'
  else:
    None

def print_hangman(word, guesses):
  mistakes, _ = check_guesses(word, guesses)
  index = min(mistakes, len(hangmans)) - 1
  if index < 0:
    return
  for line in hangmans[index]:
    print(line)

def print_guesses(guesses):
  if len(guesses) == 0:
    return
  print(f'gissade bokstäver: {" ".join(guesses)}')

def get_guess():
  guess = ''
  while len(guess) == 0:
    guess = input('Ange en bokstav: ')
  return list(guess)

def main():
  word_type = random.choice(list(ordlista.keys()))
  word = list(random.choice(ordlista[word_type]))
  guesses = []
  while not game_result(word, guesses):
    print_hangman(word, guesses)
    print_word(word_type, word, guesses)
    print_guesses(guesses)
    guesses += get_guess()
  print_word(word_type, word, word)
  if game_result(word, guesses) == 'success':
    print('Du vann!!!')
  else:
    print('Du förlorade...')

if __name__ == '__main__':
  main()
