import random

val = ["sten", "sax", "påse"]
svar =  input("sten sax påse?")
dator = random.choice(val)

print(f"användarens val: {svar}")
print(f"datorns val: {dator}")
