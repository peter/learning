def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def fibonacci(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n+1):
        previous, current = current, previous+current
    return current

def run_gcd():
    print('GCD')
    for a, b in [(2, 4), (16, 48)]:
        result = gcd(a, b)
        print(f'gcd {a}/{b} -> {result} ({a//result}/{b//result})')

def run_fibonacci():
    print('FIBONACCI')
    for n in range(0, 20):
        result = fibonacci(n)
        print(f'{n}: {result}')

if __name__ == "__main__":
    run_gcd()
    run_fibonacci()
