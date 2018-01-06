import sys
import random
import time
import re
import math

def compact(items):
    return [i for i in items if i != None]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def parse_sort_function_name(name):
    m = re.match(r'(.+)_sort$', name)
    return m and m.group(1)

def sort_function_name(name):
    return f"{name}_sort"

def current_module():
    return sys.modules[__name__]

def sort_function_names():
    return compact([parse_sort_function_name(n) for n in dir(current_module())])

def lookup_sort_function(name):
    return getattr(current_module(), sort_function_name(name))

def random_numbers(size):
    return [random.randrange(size) for _ in range(0, size)]

def merge_sort(items):
    if len(items) == 1:
        return items # base case
    split = len(items) // 2
    left = merge_sort(items[0:split])
    right = merge_sort(items[split:])
    i = 0
    j = 0
    result = []
    while i < len(left) or j < len(right):
        if j >= len(right) or (i < len(left) and left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result

def insertion_sort(items):
    result = list(items) # copy
    i = 1
    while i < len(result):
        j = i - 1
        while j >= 0 and result[j] > result[i]:
            j -= 1
        if j != i:
            result.insert(j+1, result.pop(i))
        i += 1
    return result

# Find index to place item in list of sorted items to retain ascending sort
def binary_search(sorted_items, item):
    if len(sorted_items) == 0:
        return 0
    elif len(sorted_items) == 1:
        return 0 if sorted_items[0] > item else 1
    pivot = len(sorted_items) // 2
    if sorted_items[pivot] > item:
        return binary_search(sorted_items[0:pivot], item)
    else:
        return pivot + binary_search(sorted_items[pivot:], item)

# I'm not sure insertion_binary_sort is O(NlogN). Test output:
#
# size=1000
# insertion_binary_sort elapsed=0.008890056610107422 nlog2_constant=8.920579009310614e-07
# merge_sort elapsed=0.005132436752319336 nlog2_constant=5.150058044321158e-07
# size=10000
# insertion_binary_sort elapsed=0.6642757415771484 nlog2_constant=4.9991730901664216e-06
# merge_sort elapsed=0.0631753921508789 nlog2_constant=4.754422006312347e-07
# size=30000
# insertion_binary_sort elapsed=5.621889925003051 nlog2_constant=1.260004218084712e-05
# merge_sort elapsed=0.20027585029602052 nlog2_constant=4.488675863808401e-07
# size=50000
# insertion_binary_sort elapsed=16.851253271102905 nlog2_constant=2.1590828179162007e-05
# merge_sort elapsed=0.3670228958129883 nlog2_constant=4.7025156846378976e-07
# size=80000
# insertion_binary_sort elapsed=47.66332216262818 nlog2_constant=3.657920235507824e-05
# merge_sort elapsed=0.6951335430145263 nlog2_constant=5.334800299268262e-07
def insertion_binary_sort(items):
    result = list(items) # copy
    i = 1
    while i < len(result):
        j = binary_search(result[0:i], result[i])
        if j != i:
            result.insert(j, result.pop(i))
        i += 1
    return result

def run_search_functions(search_functions, numbers):
    previous_result = None
    for name in search_functions:
        sort_function = lookup_sort_function(name)
        elapsed = []
        for _ in range(0, 5):
            start_time = time.time()
            result = sort_function(numbers)
            elapsed.append(time.time() - start_time)
        nlog2_constant = mean(elapsed)/(len(numbers)*math.log(len(numbers), 2)) if len(numbers) > 1 else None
        print(f'{sort_function_name(name)} elapsed={mean(elapsed)} nlog2_constant={nlog2_constant}')
        if not previous_result:
            previous_result = result
        elif result != previous_result:
            print(f'previous_result={previous_result}')
            print(f'result={result}')
            assert result == previous_result

def test_binary_search(max_exponent=4):
    start_exponent = 1
    for exponent in range(start_exponent, max_exponent+1):
        print(f'exponent={exponent}')
        size = 10 ** exponent
        numbers = random_numbers(size)
        elapsed = []
        for _ in range(0, 100):
            start_time = time.time()
            result = binary_search(numbers, random.randrange(size))
            elapsed.append(time.time() - start_time)
        if len(elapsed) == 1:
            print(f'elapsed={mean(elapsed)}')
        else:
            log2_expect = (elapsed[0]/math.log(10**start_exponent, 2)) * math.log(10**exponent, 2)
            print(f'elapsed={mean(elapsed)} log2_expect={log2_expect} ratio={mean(elapsed)/log2_expect}')


def test_search_functions(search_functions, max_exponent):
    for size in [10, 100, 1000, 10000, 30000, 50000, 80000, 100000]:
        print(f'size={size}')
        numbers = random_numbers(size)
        run_search_functions(search_functions, numbers)

def main():
    max_exponent = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    search_functions = sys.argv[2].split(',') if len(sys.argv) > 2 else sort_function_names()
    test_search_functions(search_functions, max_exponent)

if __name__ == "__main__":
    main()
