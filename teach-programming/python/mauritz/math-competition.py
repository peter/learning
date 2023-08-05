from random import randint

operator = input("Vilket räknesätt (*, /, +, -)? ")
low = int(input("lägsta tal? "))
high = int(input("högsta tal? "))

for i in range(0,10):
    number1 = randint(low,high)
    number2 = randint(low,high)
    expression = f"{number1} {operator} {number2}"
    answer = float(input(expression + " ? "))
    correct = eval(expression)
    print(answer,correct,answer == correct)