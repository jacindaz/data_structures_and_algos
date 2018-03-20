# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

# the prompt asks for:
# def Merge(B, C)
# def Mergesort(A)

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))

# Input:
# 5
# 2 3 9 2 9
# Output:
# 2

# the prompt asks for:
# def Mergesort(A)
# def Merge(B, C)


# SIMPLEST CASE:
# merge these 2 arrays:
#  => [38, 27] and [43, 3]
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
print(merge([3,27,38,43], [9,10,82]))
