# Uses python3 (this comment is needed for the Coursera submission)

def fibonacci(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n+1):
        previous, current = current, previous+current
    return current

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
