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

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
