# Uses python3
import sys

# Going from 1 to n is the same as going from n to 1, each time either dividing the current number by 2 or 3
# or subtracting 1 from it. Since we would like to go from n to 1 as fast as possible it is natural to repeatedly
# reduce n as much as possible.
# NOTE: moving from n to min{n/3, n/2, n − 1} is not safe
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamic_sequence(n):
    operations_count = [0] * (n + 1)

    operations_count[1] = 1
    for i in range(2, n + 1):
        count_index = [i - 1]
        if i % 2 == 0:
            count_index.append(i // 2)
        if i % 3 == 0:
            count_index.append(i // 3)

        min_count = min([operations_count[x] for x in count_index])
        operations_count[i] = min_count + 1

    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        option_list = [current_value - 1]
        if current_value % 2 == 0:
            option_list.append(current_value // 2)
        if current_value % 3 == 0:
            option_list.append(current_value // 3)

        current_value = min(
            [(c, operations_count[c]) for c in option_list],
            key=lambda x: x[1]
        )[0]
        value_trail.append(current_value)
    return reversed(value_trail)

# You are given a primitive calculator that can perform the following three operations with the current number
# x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a positive integer n, find the
# minimum number of operations needed to obtain the number n starting from the number 1.

input = sys.stdin.read()
n = int(input)
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
