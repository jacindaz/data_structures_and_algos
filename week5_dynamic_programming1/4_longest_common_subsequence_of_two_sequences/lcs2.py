# Uses python3
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

            if seq1_x_number == seq2_y_number:
                grid[y_index].append(1)
            else:
                grid[y_index].append(previous_number)

    return grid

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
                grid.append([1])
            else:
                grid.append([previous_number])

    return grid

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
                grid[y_index].append(diagonal+1)
            elif seq1_number_x != seq2_number_y:
                grid[y_index].append(longest_sequence)

    return grid

def lcs2(seq1, seq2):
    grid = construct_full_matrix(seq1, seq2)
    result = grid[-1][-1]
    return result

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
