import sys
from sort import merge_sort

def count_split_inversions(left, right):
    i = 0
    j = 0
    result = 0
    while i < len(left) or j < len(right):
        if j >= len(right) or (i < len(left) and left[i] <= right[j]):
            i += 1
        else:
            result += (len(left) - i)
            j += 1
    return result

def count_inversions(numbers):
    if len(numbers) <= 1:
        return (0, numbers)
    pivot = len(numbers) // 2
    (left_count, left) = count_inversions(numbers[0:pivot])
    (right_count, right) = count_inversions(numbers[pivot:])
    count = left_count + count_split_inversions(left, right) + right_count
    return (count, merge_sort(left + right))

def main():
    numbers = [int(l.strip()) for l in sys.stdin.readlines() if l.strip()]
    (count, _) = count_inversions(numbers)
    print(count)

# Usage:
# echo -e '3\n2\n4\n1' | python count_inversions.py
# cat ~/Dropbox/data/projects/courses/algorithms-stanford/IntegerArray.txt | python count_inversions.py
if __name__ == "__main__":
    main()
