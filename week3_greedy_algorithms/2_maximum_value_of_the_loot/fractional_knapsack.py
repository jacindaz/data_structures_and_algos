# Uses python3
import sys
# import ipdb

# 1 <= n <= 103
# 0 <= W <= 2 * 10^6
# 0 <= v <= 2 * 10^6
# 0 < w <= 2 * 10^6

def get_optimal_value(capacity, weights, values):
    max_value = 0

    print(f'capacity: {capacity}')

    # find value-to-weight ratio
    # sort as i go ???
    value_weight_ratios = []
    for index, weight in enumerate(weights):
        value = values[index]
        value_weight_ratios.append(value/weight)

    print(f'value_weight_ratios: {value_weight_ratios}')

    # find max in value_weight_ratios
    ratio_max = value_weight_ratios[0]
    ratio_max_index = 0
    for current_index, ratio in enumerate(value_weight_ratios):
        if ratio > ratio_max:
            ratio_max = ratio
            ratio_max_index = current_index
    print(f'max ratio: {ratio_max}, ratio_max_index: {ratio_max_index}')
    print(f'weights: {weights}, values: {values}')

    # reduce capacity
    if capacity >= weights[ratio_max_index]:
        print(f'\nold capacity: {capacity}, old max_value: {max_value}')

        capacity -= weights[ratio_max_index]
        max_value += values[ratio_max_index]


    print(f'new capacity: {capacity}, new max_value: {max_value}\n')

    # add to max_value


    # safe move:
    #  =>


    return max_value


print(get_optimal_value(50, [20, 50, 30], [60, 100, 120]))
# print(get_optimal_value(10, [30], [500]))
# 1 10
# 500 30

# if __name__ == "__main__":
#     data = list(map(int, sys.stdin.read().split()))
#     num_items, capacity = data[0:2]
#     values = data[2:(2 * num_items + 2):2]
#     weights = data[3:(2 * num_items + 2):2]
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))
