# Write a program that prints "Hello World!" a hundred times.

import time

start_time = time.time()

for i in range(1000000):
    print(i*i)

end_time = time.time()

print("Time elapsed: ", end_time - start_time)
