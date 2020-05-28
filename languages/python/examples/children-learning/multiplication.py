import random

while True:
  a = random.randint(2, 15)
  b = random.randint(2, 15)
  answer = int(input(f"Hur mycket är {a} * {b}?"))
  if answer == a * b:
    print("Rätt!!!")
  else:
    print("Fel, du suger, kom igen nu!")
