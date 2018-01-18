# Uses python3
import sys

def get_change(m, coins=[10, 5, 1]):
    n_coins = 0
    remainder = m
    for coin in coins:
        while remainder > 0 and remainder >= coin:
            remainder -= coin
            n_coins += 1
    return n_coins

# The goal in this problem is to find the minimum number of coins needed
# to change the input value (an integer) into coins with denominations 1, 5, and 10
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
