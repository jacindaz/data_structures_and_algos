#Uses python3
import sys

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
# print(lcs2([2,1,3,3,2], [2,5,2,2,3])) # 2
