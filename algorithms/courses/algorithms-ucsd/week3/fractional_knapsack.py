# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    make_loot = lambda w, v: {'weight': w, 'value': v, 'value_per_weight': v/w}
    sort_key = lambda l: l['value_per_weight']
    loot = sorted([make_loot(w, v) for w, v in zip(weights, values)], key=sort_key, reverse=True)
    value = 0.
    remaining = capacity
    for item in loot:
        if remaining > 0:
            fraction = (remaining/item['weight'] if item['weight'] > remaining else 1.0)
            remaining -= fraction * item['weight']
            value += fraction * item['value']
    return value

# A thief finds much more loot than his bag can fit. Help him to find the
# most valuable combination of items assuming that any fraction of a loot
# item can be put into his bag.
# Output the maximal value of fractions of items that fit into the knapsack.
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
