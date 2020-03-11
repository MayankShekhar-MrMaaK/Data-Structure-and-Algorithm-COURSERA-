# Uses python3
import sys
from collections import namedtuple
Item = namedtuple("Item", "value weight")
def get_optimal_value(capacity, weights, values):
	value=0
	weight_value_pairs = sorted([Item(v, w) for v, w in zip(values, weights)],key=lambda i: i.value / i.weight,reverse=True)
	current_weight=0
	final_value=0.0
	for i in weight_value_pairs:
		if current_weight+i.weight<=capacity:
			current_weight+=i.weight
			final_value+=i.value
		else:
			remain=capacity-current_weight
			final_value+=i.value*(remain/i.weight)
			break
	return final_value
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
