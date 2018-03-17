# Uses python3
import sys

def get_majority_element(numbers, left, right):
    max_count = 0
    results = {}
    majority_element = -1

    for number in numbers:
        results[number] = 0

    for number in numbers:
        results[number] += 1
        if results[number] > max_count:
            max_count = results[number]

    if max_count > (len(numbers)/2):
        majority_element = 1

    return majority_element

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
