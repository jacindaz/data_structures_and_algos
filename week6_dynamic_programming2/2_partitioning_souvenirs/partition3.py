# Uses python3
import sys
import itertools
# import ipdb

def partition3(array):
    count = 0
    for something in itertools.product(range(3), repeat=len(array)):
        sums = [None] * 3
        print('---------------------------')
        print(f'something: {something}, array: {array}')

        for i in range(3):
            sums[i] = sum(array[k] for k in range(len(array)) if something[k] == i)
            print(f'i: {i}, sums: {sums}')

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

blah = [17,59,34,57,17,23,67,1,18,2,59]
print(partition3(blah))
