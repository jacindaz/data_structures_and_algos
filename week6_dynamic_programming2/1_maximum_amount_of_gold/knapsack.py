# Uses python3
import sys

def greedy_solution(max_capacity, items):
    result=0
    items = sorted(items, reverse=True)

    for item in items:
        if max_capacity > 0:
            max_item = max(items)
            if max_capacity - max_item >= 0:
                result += max_item
                max_capacity -= max_item
                items.remove(max_item)

    return result

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

print(starter_grid(10, [1,4,8]))

