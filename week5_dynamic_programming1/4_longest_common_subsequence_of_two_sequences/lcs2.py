#Uses python3
import sys
from random import *

def brute_force(s1, s2, i, j):
    if(i == -1 or j == -1):
        return 0
    if(s1[i] == s2[j]):
        return 1 + brute_force(s1, s2, i-1, j-1)
    return max(brute_force(s1, s2, i-1, j), brute_force(s1, s2, i, j-1))


# string1, string2 = [[2,7,5], [2,5]] # 2
# string1, string2 = [[2,7,8,3], [5,2,8,7,3]] # 3
# string1, string2 = [[7], [1,2,3,4]] # 0
# string1, string2 = [[1,2,3,4], [5,6,7,10,2,2,2,2,3]] # 2
# string1, string2 = [[2,1,3,3,2], [2,5,2,2,3]] # 2
# string1, string2 = [[1,2,2,2,6], [5,6,7,10,2,2,2,2,3]] # 3
# print(brute_force(string1, string2, len(string1)-1, len(string2)-1))

def stress_testing_random_input():
    s1_length = randint(1, 20)
    s2_length = randint(1, 20)
    # print(f's1_length: {s1_length}, s2_length: {s2_length}')

    if s1_length > 3 and s2_length > 3:
        num_dupes = randint(2, min(s1_length, s2_length))
        dupe_value = randint(1,50)
        # print(f'num_dupes: {num_dupes}, dupe_value: {dupe_value}')
    else:
        num_dupes = randint(1, 2)
        dupe_value = randint(1,50)
        # print(f'num_dupes: {num_dupes}, dupe_value: {dupe_value}')

    s1 = []
    for n in range(1,s1_length-num_dupes):
        s1.append(randint(1,50))
    # print(f'\ns1: {s1}, s1_length-num_dupes: {s1_length-num_dupes}')

    s2 = []
    for n in range(1,s2_length-num_dupes):
        s2.append(randint(1,50))
    # print(f's2: {s2}, s2_length-num_dupes: {s2_length-num_dupes}')

    # s1: append dupes at random index
    for n in range(1,num_dupes):
        # print('------------------------------------------------------')

        random_index = randint(0,s1_length-1)
        # print(f'random_index: {random_index}, s1_length: {s1_length}')
        # print(f'old s1: {s1}')

        s1.insert(random_index, dupe_value)
        # print(f's1 with new dupe value: {s1}')

    # s2: append dupes at random index
    for n in range(1,num_dupes):
        # print('------------------------------------------------------')

        random_index = randint(0,s2_length-1)
        # print(f'random_index: {random_index}, s2_length: {s2_length}')
        # print(f'old s2: {s2}')

        s2.insert(random_index, dupe_value)
        # print(f's2 with new dupe value: {s2}')

    # print(f'\ns1 length: {s1_length} \ts1: {s1}')
    # print(f's2 length: {s2_length} \ts2: {s2}')

    return [s1, s2]

# print(stress_testing_random_input())




def starter_grid_x(sequence1_x, sequence2_y):
    grid = []
    y_index = 0

    for x_index, seq1_x_number in enumerate(sequence1_x):
        seq2_y_number = sequence2_y[y_index]

        if x_index == 0 and y_index == 0:
            if seq1_x_number == seq2_y_number:
                grid.append([1])
            else:
                grid.append([0])
        else:
            previous_number = grid[y_index][x_index-1]
            grid[y_index].append(previous_number)

    return grid

# print(starter_grid_x([2,1,3,3,2], [2,5,2,2,3]))

def starter_grid(sequence1_x, sequence2_y):
    grid = starter_grid_x(sequence1_x, sequence2_y)
    x_index = 0

    for y_index in range(1, len(sequence2_y)):
        seq2_y_number = sequence2_y[y_index]
        seq1_x_number = sequence1_x[x_index]
        previous_number = grid[y_index-1][x_index]

        if grid[0][0] == 1:
            grid.append([1])
        else:
            if seq1_x_number == seq2_y_number:
                grid.append([previous_number+1])
            else:
                grid.append([previous_number])

    return grid
# print(starter_grid([2,1,3,3,2], [2,5,2,2,3]))
# print(starter_grid([1,3,2], [2,5,2,2,3])) # 1
# print(starter_grid([5,3,2], [2,5,2,2,3])) # 2


def construct_full_matrix(sequence1_x, sequence2_y):
    grid = starter_grid(sequence1_x, sequence2_y)

    for x_index in range(1,len(sequence1_x)):
        seq1_number_x = sequence1_x[x_index]

        for y_index in range(1, len(sequence2_y)):
            seq2_number_y = sequence2_y[y_index]

            above = grid[y_index-1][x_index]
            diagonal = grid[y_index-1][x_index-1]
            left = grid[y_index][x_index-1]

            longest_sequence = max(above, diagonal, left)

            if seq1_number_x == seq2_number_y:
                # grid[y_index].append(longest_sequence+1)
                grid[y_index].append(diagonal+1)
            elif seq1_number_x != seq2_number_y:
                grid[y_index].append(longest_sequence)
                # grid[y_index].append(diagonal)

    return grid

# print(construct_full_matrix([2,1,3,3,2], [2,5,2,2,3])) # 2
# print(construct_full_matrix([1,3,2], [2,5,2,2,3])) # 1
# print(construct_full_matrix([5,3,2], [2,5,2,2,3])) # 2


def lcs2(seq1, seq2):
    grid = construct_full_matrix(seq1, seq2)
    result = grid[-1][-1]
    return result


# print(lcs2([2,7,5], [2,5])) # 2
# print(lcs2([2,7,8,3], [5,2,8,7,3])) # 3
# print(lcs2([7], [1,2,3,4])) # 0
# print(lcs2([1,2,3,4], [5,6,7,10,2,2,2,2,3])) # 2
# print(lcs2([1,2,2,2,6], [5,6,7,10,2,2,2,2,3])) # 3
# print(lcs2([2,1,3,3,2], [2,5,2,2,3])) # 2

for n in range(1,20):
    seq1, seq2 = stress_testing_random_input()

    brute_force_result = brute_force(seq1, seq2, len(seq1)-1, len(seq2)-1)
    optimized_result = lcs2(seq1, seq2)

    if brute_force_result != optimized_result:
        print('----------------------')
        print('does not match!!!')
        print(f'brute_force_result: {brute_force_result} \toptimized_result: {optimized_result}')
        print(f'seq1: {seq1}')
        print(f'seq2: {seq2}')
