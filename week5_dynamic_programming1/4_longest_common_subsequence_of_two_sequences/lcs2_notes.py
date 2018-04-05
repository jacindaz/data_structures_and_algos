#Uses python3

import sys

def construct_grid(sequence1, sequence2):
    grid = []
    coordinates = []

    # SMALLEST UNIT OF WORK
    # JUST MAKE GRID WORK, SEE LATER IF IT WORKS OR HOW TO OPTIMIZE

    for index1, number1 in enumerate(sequence1):
        row = []
        for index2, number2 in enumerate(sequence2):
            if number1 == number2:
                coordinates.append((index1, index2))
                row.append(number1)
            elif number1 != number2:
                row.append(None)
        grid.append(row)

    print(f'grid: {grid}')

    return coordinates

print(construct_grid([2,7,8,3], [5,2,8,7,3]))
# print(construct_grid([2,7,5], [2,5]))

def lcs2(a, b):
    #write your code here
    return min(len(a), len(b))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

# Input:
# 3
# 2 7 5
# 2
# 2 5
# Output:
# 2
# A common subsequence of length 2 is (2, 5).

# Input:
# 1
# 7
# 4
# 1 2 3 4
# Output:
# 0
# The two sequences do not share elements.

# Input:
# 4
# 2 7 8 3
# 4
# 5 2 8 7
# Output:
# 2
# One common subsequence is (2, 7). Another one is (2, 8).


#Uses python3

import sys

def coordinates_of_matches(sequence1, sequence2):
    coordinates = []

    for index1, number1 in enumerate(sequence1):
        for index2, number2 in enumerate(sequence2):
            if number1 == number2:
                coordinates.append((index1, index2))
    return coordinates

# print(construct_grid([2,7,8,3], [5,2,8,7,3]))
# print(construct_grid([2,7,5], [2,5]))

# [
#     [-, 2, -, -, -],
#     [-, -, -, 7, -],
#     [-, -, 8, -, -],
#     [-, -, -, -, 3]
# ]

def are_matches_sequences(matches_coords):
    if len(matches_coords) <= 1:
        max_sequence_length = len(matches_coords)
    else:
        max_sequence_length = 1
        first_coord = matches_coords[0]

        for second_coord in matches_coords[1:]:
            print('\n------------------\n')
            print(f'first_coord: {first_coord}, second_coord: {second_coord}')
            print(f'max_sequence_length: {max_sequence_length}')

            if first_coord[0] <= second_coord[0] and first_coord[1] <= second_coord[1]:
                max_sequence_length += 1

    return max_sequence_length
print(are_matches_sequences([(0,1),(1,3),(2,2),(3,4)])) # 3



def lcs2(sequence1, sequence2):
    sub_sequences1 = find_sequences(sequence1)
    sub_sequences2 = find_sequences(sequence2)

    sub_sequences1 = sorted(sub_sequences1, key=lambda sub_seq: (sub_seq[0],sub_seq[1]))
    sub_sequences2 = sorted(sub_sequences2, key=lambda sub_seq: (sub_seq[0],sub_seq[1]))

    num_common_sub_sequence = 0
    for sub_seq1 in sub_sequences1:
        for sub_seq2 in sub_sequences2:
            if sub_seq1 == sub_seq2:
                # print(f'sub_seq1: {sub_seq1}, sub_seq2: {sub_seq2}')
                num_common_sub_sequence += 1

    return num_common_sub_sequence

# print(lcs2([7], [1,2,3,4])) # 0
# print(lcs2([2,7,8,3], [5,2,8,7])) # 2
# print(lcs2([2,7,5], [2,5])) # 2
# print(lcs2([1,2,3], [3,2,1])) # 1


# print(lcs([1,2,3], [1,2,3,4])) # 3
# print(lcs([-4,1,2,3], [1,2,3,-4])) # 3
