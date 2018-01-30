# Uses python3 (this comment is needed for the Coursera submission)

def fibonacci(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n+1):
        previous, current = current, previous+current
    return current

def fibonacci_period_length(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_modulo(n, m):
    remainder = n % fibonacci_period_length(m)
    return fibonacci(remainder) % m

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_modulo(n, m))
