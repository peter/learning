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

# It seems insertion_binary_sort is not O(NlogN). Test output:
#
# size=10
# insertion_binary_sort elapsed=2.002716064453125e-05 nlog2_constant=6.028776081985097e-07
# insertion_sort elapsed=1.0776519775390626e-05 nlog2_constant=3.2440557012586476e-07
# merge_sort elapsed=3.204345703125e-05 nlog2_constant=9.646041731176154e-07
# size=100
# insertion_binary_sort elapsed=0.00034413337707519533 nlog2_constant=5.179723450438863e-07
# insertion_sort elapsed=0.0003197193145751953 nlog2_constant=4.812255194013104e-07
# merge_sort elapsed=0.0003436088562011719 nlog2_constant=5.171828624617216e-07
# size=1000
# insertion_binary_sort elapsed=0.0083221435546875 nlog2_constant=8.350716127275357e-07
# insertion_sort elapsed=0.031513309478759764 nlog2_constant=3.1621504719162495e-06
# merge_sort elapsed=0.004467201232910156 nlog2_constant=4.4825385592435855e-07
# size=10000
# insertion_binary_sort elapsed=0.6656803607940673 nlog2_constant=5.0097439030858885e-06
# insertion_sort elapsed=3.458074760437012 nlog2_constant=2.602460575350191e-05
# merge_sort elapsed=0.0655287742614746 nlog2_constant=4.931531657949426e-07
# size=30000
# insertion_binary_sort elapsed=5.8100584030151365 nlog2_constant=1.3021774159182998e-05
# insertion_sort elapsed=31.56323504447937 nlog2_constant=7.07409960404403e-05
# merge_sort elapsed=0.20908894538879394 nlog2_constant=4.686199065781626e-07
# size=50000
# insertion_binary_sort elapsed=16.143204307556154 nlog2_constant=2.068363372493189e-05
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


def test_search_functions(search_functions):
    for size in [10, 100, 1000, 10000, 30000, 50000, 80000, 100000]:
        print(f'size={size}')
        numbers = random_numbers(size)
        run_search_functions(search_functions, numbers)

def main():
    search_functions = sys.argv[1].split(',') if len(sys.argv) > 1 else sort_function_names()
    test_search_functions(search_functions)

if __name__ == "__main__":
    main()
