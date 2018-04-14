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

def partition3_dp(array):
    array_sum = sum(array)
    # if the sum is evenly divisible by 3
    # find the partition
    # if array_sum % 3 == 0:
    #     partition = int(array_sum/3)
    # # if the sum is not divisible by 3, return 0
    # else:
    #     return 0
    partition = int(array_sum/2)

    grid = [[0 for x in range(0,len(array)+1)] for x in range(0,partition+1)]
    print(f'grid: {grid}')

    for array_index in range(len(array)+1):
        for partition_sum in range(partition+1):
            sub_array = array[:array_index]
            sub_array_sum = sum(sub_array)

            print('-----------------')
            print(f'array_index: {array_index}, partition_sum: {partition_sum}')
            print(f'sub_array: {sub_array}, sub_array_sum: {sub_array_sum}')
            if array_index == 0 and partition_sum == 0:
                grid[partition_sum][array_index] = True

            # if subset of array can find sum of partition, true
            #  => if includes actual partition_sum number
            #  => if sum(subset) == partition_sum
            #  => if prior cell == True
            elif grid[partition_sum][array_index-1] == True:
                grid[partition_sum][array_index] = True
            elif sub_array_sum >= partition_sum:
                grid[partition_sum][array_index] = True
            else:
                grid[partition_sum][array_index] = False

    print(f'grid: {grid}')


def partition2_dp(array):
    n = len(array)
    K = sum(array)
    partition = int(K/2)
    print(f'partition: {partition}')

    grid = [[0 for x in range(0,n+1)] for x in range(0,partition+1)]
    print(f'original grid: {grid}\n')

    for i in range(len(grid[0])):
        grid[0][i] = True
    print(f'\ninitialize top row with True.----------\n{grid}\n')

    for i in range(len(grid)):
        if i == 0:
            grid[i][0] = True
        else:
            grid[i][0] = False
    print(f'\nintialize leftmost column to False.----------\n{grid}\n')

    for array_index in range(1,n+1):
        for current_partition in range(1,partition+1):
            if current_partition-array[array_index-1] >= 0:
                grid[current_partition][array_index] = grid[current_partition][array_index-1] or grid[current_partition-array[array_index-1]][array_index-1]
            else:
                grid[current_partition][array_index] = grid[current_partition][array_index-1]

    return grid

# a = [17,59,34,57,17,23,67,1,18,2,59]
# b = [3,1,1,2,2,3] # sum: 12, partition: 4, return: 1
c = [3,1,1,2,2,1] # sum: 10, partition: none, return: 0
print(partition_wikipedia(c))

# [
#     [True, True, True, True, True, True, True],
#     [False, False, True, True, True, True, True],
#     [False, False, False, True, True, True, True],
#     [False, True, True, True, True, True, True],
#     [False, False, True, True, True, True, True],
#     [False, False, False, True, True, True, True]
# ]
