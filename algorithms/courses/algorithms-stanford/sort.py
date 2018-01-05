import sys
import random
import time
import re

def compact(items):
    return [i for i in items if i != None]

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

def insertion_binary_sort(items):
    result = list(items) # copy
    i = 1
    while i < len(result):
        j = binary_search(result[0:i], result[i])
        # print(f'debug insertion_binary_sort i={i} j={j} result={result} result[j]={result[j]} result[i]={result[i]}')
        if j != i:
            result.insert(j, result.pop(i))
        i += 1
    return result

def run_search_functions(search_functions, numbers):
    previous_result = None
    for name in search_functions:
        start_time = time.time()
        result = lookup_sort_function(name)(numbers)
        elapsed = time.time() - start_time
        print(f'{sort_function_name(name)} elapsed={elapsed}')
        if not previous_result:
            previous_result = result
        elif result != previous_result:
            print(f'previous_result={previous_result}')
            print(f'result={result}')
            assert result == previous_result

def test_binary_search(max_exponent):
    for exponent in range(0, max_exponent+1):
        print(f'exponent={exponent}')
        size = 10 ** exponent
        numbers = random_numbers(size)
        start_time = time.time()
        result = binary_search(numbers, random.randrange(size))
        elapsed = time.time() - start_time
        print(f'result={result} elapsed={elapsed}')

def test_search_functions(search_functions, max_exponent):
    for exponent in range(0, max_exponent+1):
        print(f'exponent={exponent}')
        size = 10 ** exponent
        numbers = random_numbers(size)
        run_search_functions(search_functions, numbers)

def main():
    max_exponent = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    search_functions = sys.argv[2].split(',') if len(sys.argv) > 2 else sort_function_names()
    test_search_functions(search_functions, max_exponent)

if __name__ == "__main__":
    main()
