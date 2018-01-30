import sys
from sort import quick_sort

def main():
    strategy = sys.argv[1] if len(sys.argv) > 1 else 'first'
    numbers = [int(l.strip()) for l in sys.stdin.readlines() if l.strip()]
    assert numbers[0] == 2148
    assert numbers[-1] == 9269
    cost = quick_sort(numbers, strategy=strategy)
    print(cost)

if __name__ == "__main__":
    main()
