from random import randint
import time

operator = input("Vilket räknesätt (*, /, +, -)? ")
low = int(input("lägsta tal? "))
high = int(input("högsta tal? "))

correct_count = 0
all_elepsed = []
for i in range(0,5):
    number1 = randint(low,high)
    number2 = randint(low,high)
    expression = f"{number1} {operator} {number2}"
    start_time = time.time()
    answer = float(input(expression + " ? "))
    elapsed = time.time() - start_time
    all_elepsed.append(elapsed)
    correct = eval(expression)
    if answer == correct:
        print ("rätt",elapsed)
        correct_count += 1
    else:
        print("fel, rätt svar: ",correct)
print("antal rätt",correct_count)
print("total tid",sum(all_elepsed))
print("max tid",max(all_elepsed))
print("min tid",min(all_elepsed))



