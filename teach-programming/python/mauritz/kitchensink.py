#a = 5
#print(a)
#a = a * 3
#print(a)
numbers = [1, 23, 52]
big_numbers = []
small_numbers = []
for i in numbers: 
    if i > 50:
        big_numbers.append(i)
    else:
        small_numbers.append(i)
        
print("big", big_numbers)
print("small", small_numbers)
