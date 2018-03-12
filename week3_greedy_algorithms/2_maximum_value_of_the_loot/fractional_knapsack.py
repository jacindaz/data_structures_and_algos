# Uses python3
import sys

def ratio_and_sort(weights, values):
    ratios = []
    for index, weight in enumerate(weights):
        ratio = values[index]/weight
        ratios.append(
            { 'weight': weight, 'value': values[index], 'ratio': ratio }
        )

    return sorted(ratios, key=lambda k: k['ratio'], reverse=True)

def fractional_knapsack(capacity, weights, values):
    sorted_values = ratio_and_sort(weights, values)
    max_value = 0

    for item in sorted_values:
        if capacity == 0:
            return max_value
        elif capacity - item['weight'] >= 0:
            max_value += item['value']
            capacity -= item['weight']
        else:
            percentage_weight = capacity/item['weight']
            fractional_value = item['value'] * percentage_weight

            max_value += fractional_value
            item['weight'] = item['weight'] - capacity
            capacity = 0

    return round(max_value, 3)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    num_items, capacity = data[0:2]
    values = data[2:(2 * num_items + 2):2]
    weights = data[3:(2 * num_items + 2):2]
    opt_value = fractional_knapsack(capacity, weights, values)
    print("{:.10f}".format(opt_value))
