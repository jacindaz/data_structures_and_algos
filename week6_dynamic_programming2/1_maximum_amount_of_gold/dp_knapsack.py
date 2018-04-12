# Uses python3
import sys

def optimal_weight(max_capacity, items):
    values = items
    weights = items

    num_items = len(items)
    max_capacities_grid = [[0 for x in range(max_capacity+1)] for x in range(num_items+1)]

    for item_index in range(1,num_items+1):
        current_item = items[item_index-1]

        for capacity in range(1,max_capacity+1):
            prev_item_index = item_index-1
            previous_item_weight = weights[prev_item_index]
            previous_item_value = values[prev_item_index]

            max_capacity_one_less_item = max_capacities_grid[prev_item_index][capacity]
            if previous_item_weight <= capacity:
                part1 = max_capacities_grid[prev_item_index][capacity-previous_item_weight]
                max_capacities_grid[item_index][capacity] = max(previous_item_value + part1, max_capacity_one_less_item)
            else:
                max_capacities_grid[item_index][capacity] = max_capacity_one_less_item

    return max_capacities_grid[num_items][max_capacity]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
