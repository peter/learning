# Uses python3
import sys

def binary_search(sorted_items, item):
    if len(sorted_items) == 0:
        return -1
    elif len(sorted_items) == 1:
        return 0 if sorted_items[0] == item else -1
    pivot = len(sorted_items) // 2
    if sorted_items[pivot] > item:
        return binary_search(sorted_items[0:pivot], item)
    else:
        offset = binary_search(sorted_items[pivot:], item)
        return pivot + offset if offset >= 0 else offset

def binary_search_iterative(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search_iterative(a, x), end = ' ')
