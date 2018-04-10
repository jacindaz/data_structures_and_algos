# import ipdb

def starter_grid(max_capacity, items):
    grid = []

    # fill in top row with zeroes
    for n in range(0,max_capacity+1):
        if n == 0:
            grid.append([0])
        else:
            grid[0].append(0)

    # fill in y-axis columns
    for n in range(1,len(items)+1):
        grid.append([0])

    return grid

def knapsack_dp_solution(max_capacity, items):
    grid = starter_grid(max_capacity, items)
    print(f'starter_grid: {grid}')
    combination_available_capacities = []

    for item_index, current_item in enumerate(items, start=1):
        for capacity in range(1,max_capacity+1):
            print('-----------------')
            print(f'item_index: {item_index}, current_item: {current_item}')
            print(f'capacity: {capacity}')

            # if capacity of all available items
            # is less than max_capaity
            # append to item
            if current_item == capacity:
                grid[item_index].append(current_item)
                print('\nadding to the grid. current_item <= capacity')
                print(f'grid: {grid}')

            # if capacity-current_item is > 0
            # can i add another item ? if so, which item?
            elif (capacity - current_item) > 0:
                print('something!')

            # if not... ? take capacity from item above
            else:
                item_from_above = grid[item_index-1][capacity]
                grid[item_index].append(item_from_above)

    return grid

print(knapsack_dp_solution(10, [1,4,8])) # 9

[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4],
    [0, 1, 1, 1, 4, 4, 4, 4, 8, 8, 8]
]
