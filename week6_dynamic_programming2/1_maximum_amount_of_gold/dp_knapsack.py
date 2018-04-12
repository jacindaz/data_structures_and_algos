# import ipdb
def knapsack(max_capacity, items):
    # assigning for understanding purposes
    # since item weights and values are the same (because it's gold)
    values = items
    weights = items

    num_items = len(items)
    max_capacities_grid = [[0 for x in range(max_capacity+1)] for x in range(num_items+1)]

    for item_index in range(1,num_items+1):
        current_item = items[item_index-1]
        for capacity in range(1,max_capacity+1):
            print('-------------')
            print(f'item_index: {item_index}, capacity: {capacity}, current_item: {current_item}')

            prev_item_index = item_index-1
            previous_item_weight = weights[prev_item_index]
            previous_item_value = values[prev_item_index]

            value_above = max_capacities_grid[prev_item_index][capacity]
            if previous_item_weight <= capacity:
                part1 = max_capacities_grid[prev_item_index][capacity-previous_item_weight]
                max_capacities_grid[item_index][capacity] = max(previous_item_value + part1, value_above)
                print(f'previous_item_weight <= capacity. max({previous_item_value} + {part1}, {value_above})')

            else:
                max_capacities_grid[item_index][capacity] = value_above
                print(f'previous_item_weight NOT <= capacity. filling in value above: {value_above}')

    print(f'\nfinal grid: {max_capacities_grid}\n')
    return max_capacities_grid[num_items][max_capacity]

print(knapsack(10, [2,4,7]))

   # current capacity
# [  # 0  1  2  3  4  5  6  7  8  9  10  # item index
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
#     [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2], # 1
#     [0, 0, 2, 2, 4, 4, 6, 6, 6, 6, 6], # 2
#     [0, 0, 2, 2, 4, 4, 6, 7, 7, 9, 9]  # 3
# ]
