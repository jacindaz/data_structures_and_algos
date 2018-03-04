# Uses python3

def max_pairwise(array):
    largest_number = array[0]

    if len(array) == 2:
        product = array[0]*array[1]
        return product
    else:
        for i in array:
            if abs(i) >= abs(largest_number):
                largest_number = i

        array.remove(largest_number)

        second_largest = array[0]
        for i in array:
            if abs(i) >= abs(second_largest):
                second_largest = i

        product = largest_number*second_largest

    return product

n = int(input())
array = [int(x) for x in input().split()]

largest_number = array[0]

if len(array) == 2:
    print(array[0]*array[1])
else:
    for i in array:
        if abs(i) >= abs(largest_number):
            largest_number = i

    array.remove(largest_number)

    second_largest = array[0]
    for i in array:
        if abs(i) >= abs(second_largest):
            second_largest = i

    print(largest_number*second_largest)
