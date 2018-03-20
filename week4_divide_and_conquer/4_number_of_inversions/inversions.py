# Uses python3
import sys

def binary_search(sorted_numbers, number):
    result = -1

    low, high = 0, len(sorted_numbers)-1
    key_not_found = True

    while low <= high:
        midpoint = low + ((high - low) // 2)
        number_at_midpoint = sorted_numbers[midpoint]

        if number_at_midpoint < number:
            low = midpoint + 1
        elif number_at_midpoint > number:
            high = midpoint - 1
        elif number_at_midpoint == number:
            result = midpoint
            break

    return result

# print(binary_search([2,2,3,9,9], 3))

def merge(array1, array2):
    merged_array = []

    while len(array1) > 0 and len(array2) > 0:
        first_el_a1 = array1[0]
        first_el_a2 = array2[0]

        print('\n-----------------------------------\n')
        print(f'array 1: {first_el_a1}, array 2: {first_el_a2}')
        print(f'array 1: {array1}, array 2: {array2}')
        print(f'merged_array: {merged_array}')

        if first_el_a1 <= first_el_a2:
            merged_array.append(first_el_a1)
            array1 = array1[1:]
        elif first_el_a1 > first_el_a2:
            merged_array.append(first_el_a2)
            array2 = array2[1:]

    if len(array1) > 0:
        print(f'\nthere"s some left overs! array 1: {array1}\n')
        merged_array = merged_array + array1
    elif len(array2) > 0:
        print(f'\nthere"s some left overs! array 2: {array2}\n')
        merged_array = merged_array + array2

    print('\n-----------------------------------\n')
    return merged_array

# print(merge([2,3],[9,2,9]))
# print(merge([27, 38], [3,43]))
# print(merge([3,27,38,43], [9,10,82]))
# print(merge([38,27,43],[39,82,10]))
# print(merge([2,2,2,2,2,2,2,2,99],[2,2,1,0,2,2,2,2,2,-44]))

def merge_sort(array_to_sort):
    array_length = len(array_to_sort)

    if array_length == 1:
        return array_to_sort

    midpoint = array_length//2

    array_left_half = merge_sort(array_to_sort[:midpoint])
    array_right_half = merge_sort(array_to_sort[midpoint:])

    sorted_array = merge(array_left_half, array_right_half)

    print('\n-----------------------------------\n')
    print(f'sorted_array: {sorted_array}')
    print(f'midpoint: {midpoint}, array_left_half: {array_left_half}')
    print(f'array_right_half: {array_right_half}')

    print('\n-----------------------------------\n')

    return sorted_array

# print(merge_sort([38,27,43,39,82,10])) # 7 inversions
# print(merge_sort([2,3,9,2,9])) # 2 inversions
# print(merge_sort([2,2,2,2,2,2,2,2,99,2,2,1,0,2,2,2,2,2,-44]))

def get_number_of_inversions(original_array, sorted_array, num_inversions=0):
    if len(original_array) == 0 or len(sorted_array) == 0:
        return num_inversions

    current_number = original_array[0]

    print('\n-----------------------------------\n')
    print(f'num_inversions: {num_inversions}, current_number: {current_number}')
    print(f'original array: {original_array}, sorted_array: {sorted_array}')

    # binary search in sorted array, binary_search(sorted_numbers, number):
    sorted_array_current_num_index = binary_search(sorted_array, current_number)
    print(f'sorted_array_current_num_index: {sorted_array_current_num_index}')

    # find what index that number is in in the sorted array
    # the index is the number of inversions
    num_inversions += sorted_array_current_num_index
    print(f'added inversions! num_inversions: {num_inversions}')

    # remove the current_number from the original and the sorted array
    original_array = original_array[1:]
    sorted_array.remove(current_number)

    # repeat
    get_number_of_inversions(original_array, sorted_array, num_inversions)

# print(get_number_of_inversions([2,3,9,2,9], [2,2,3,9,9]))
print(get_number_of_inversions([38,27,43,39,82,10],[10,27,38,39,43,82]))
