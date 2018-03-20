# Uses python3
import sys

def merge(array1, array2):
    merged_array = []

    while len(array1) > 0 and len(array2) > 0:
        first_el_a1 = array1[0]
        first_el_a2 = array2[0]

        print('\n-----------------------------------\n')
        print(f'array 1 first element: {first_el_a1}')
        print(f'array 2 first element: {first_el_a2}')
        print(f'array 1: {array1}, array 2: {array2}')
        print(f'merged_array: {merged_array}')

        if first_el_a1 <= first_el_a2:
            merged_array.append(first_el_a1)
            array1 = array1[1:]
        else:
            merged_array.append(first_el_a2)
            array2 = array2[1:]

    if len(array1) > 0:
        merged_array.append(array1[0])
    elif len(array2) > 0:
        merged_array.append(array2[0])

    print('\n-----------------------------------\n')
    return merged_array

# print(merge([27, 38], [3,43]))
# print(merge([3,27,38,43], [9,10,82]))


def merge_sort(array_to_sort, index=0):
    array_length = len(array_to_sort)

    if array_length == 1:
        return array_to_sort

    midpoint = array_length//2
    array_left_half = merge_sort(array_to_sort[:midpoint], index+1)
    array_right_half = merge_sort(array_to_sort[midpoint:], index+1)
    sorted_array = merge(array_left_half, array_right_half)

    return sorted_array

print(merge_sort([38,27,43,39,82,10]))
