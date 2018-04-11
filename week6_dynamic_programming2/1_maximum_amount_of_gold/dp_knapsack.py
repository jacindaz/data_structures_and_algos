# import ipdb


def knapsack(max_capacity, items):
    # assigning for understanding purposes
    # since item weights and values are the same (because it's gold)
    values = items
    weights = items

    num_items = len(items)
    max_capacities_grid = [[0 for x in range(max_capacity+1)] for x in range(num_items+1)]
    print(f'max_capacities_grid: {max_capacities_grid}')

    for item_index in range(1,num_items+1):
        current_item = items[item_index-1]
        for capacity in range(1,max_capacity+1):
            print('-------------')
            print(f'item_index: {item_index}, capacity: {capacity}, current_item: {current_item}')
            print(f'max_capacities_grid: {max_capacities_grid}')

            if item_index == 0 or capacity == 0:
                max_capacities_grid[item_index][capacity] = 0
            elif weights[item_index-1] <= capacity:
                max_capacities_grid[item_index][capacity] = max(
                    values[item_index-1] + max_capacities_grid[item_index-1][capacity-weights[item_index-1]],
                    max_capacities_grid[item_index-1][capacity]
                )
            else:
                max_capacities_grid[item_index][capacity] = max_capacities_grid[item_index-1][capacity]

    print(f'\nfinal grid: {max_capacities_grid}\n')
    return max_capacities_grid[num_items][max_capacity]

print(knapsack(10, [2,4,7]))
