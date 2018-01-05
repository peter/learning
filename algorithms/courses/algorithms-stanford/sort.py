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

def run_search_functions(numbers):
    previous_result = None
    for name in sort_function_names():
        start_time = time.time()
        result = lookup_sort_function(name)(numbers)
        elapsed = time.time() - start_time
        print(f'{sort_function_name(name)} elapsed={elapsed}')
        if previous_result:
            assert result == previous_result

def main():
    for exponent in range(0, 5):
        print(f'exponent={exponent}')
        size = 10 ** exponent
        numbers = random_numbers(size)
        run_search_functions(numbers)

if __name__ == "__main__":
    main()
