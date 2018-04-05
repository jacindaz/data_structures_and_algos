# Uses python3
import sys

def greedy_solution(max_capacity, items):
    result=0
    items = sorted(items, reverse=True)
    print(f'items: {items}')

    for item in items:
        print('-----------------------')
        print(f'item: {item}, items: {items}')

        if max_capacity > 0:
            max_item = max(items)
            print(f'max_item: {max_item}')

            if max_capacity - max_item >= 0:
                result += max_item
                max_capacity -= max_item
                items.remove(max_item)

                print(f'result: {result}, max_capacity: {max_capacity}')
                print(f'updated items: {items}')

    return result

print(greedy_solution(10, [1,4,8]))
