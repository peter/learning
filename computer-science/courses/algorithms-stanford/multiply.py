import sys

def to_digits(n):
    return [int(x) for x in str(n)]

def from_digits(digits):
    return int(''.join([str(i) for i in digits]))

# Karatsuba multiplication algorithm
# Assumption: n1 and n2 are same length?
# Assumption: n1 and n2 are power of 2?
# n1 = 10^n/2*a + b
# n2 = 10^n/2*c + d
# n1 * n2 = (10^n/2*a + b) * (10^n/2*c + d) = 10^n*ac + 10^n/2(ad + bc) + bd
# (a + b) * (c + d) = ac + ad + bc + bd
# ad + bc = (a + b) * (c + d) - ac - bd
def multiply(n1, n2):
    n1_digits = to_digits(n1)
    n2_digits = to_digits(n2)
    if len(n1_digits) == 1 or len(n2_digits) == 1:
        return n1 * n2 # base case
    l1 = len(n1_digits) // 2
    l2 = len(n2_digits) // 2
    # print(f'debug n1={n1} n2={n2} l1={l1} l2={l2} a_digits={n1_digits[0:l1]} b_digits={n1_digits[l1:]}')
    a = from_digits(n1_digits[0:l1])
    b = from_digits(n1_digits[l1:])
    c = from_digits(n2_digits[0:l2])
    d = from_digits(n2_digits[l2:])
    ac = multiply(a, c)
    bd = multiply(b, d)
    abcd = multiply((a + b), (c + d))
    ad_plus_bc = abcd - ac - bd
    return (10 ** len(n1_digits)) * ac + (10 ** l1) * ad_plus_bc + bd

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

result = multiply(n1, n2)

print(f"{n1}*{n2}={result}")
