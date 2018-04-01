#Uses python3
import sys
def starter_grid_x(sequence1_x, sequence2_y):
    grid = []

    y_index = 0
    for x_index, seq1_x_number in enumerate(sequence1_x):
        print('\n------------------\n')
        print(f'x_index: {x_index}, y_index: {y_index}')
        print(f'grid: {grid}')

        if x_index == 0 and y_index == 0:
            grid.append([0])

            print('x and y index are 0')
            print(f'y_index: {y_index}')
        else:
            seq2_y_number = sequence2_y[y_index]
            previous_number = grid[y_index][x_index-1]

            print(f'\nx and y index are not 0')
            print(f'seq1_x_number: {seq1_x_number}, seq2_y_number: {seq2_y_number}')
            print(f'previous_number: {previous_number}')
            print(f'grid[y_index]: {grid[y_index]}')
            print(f'\ngrid: {grid}')

            if seq1_x_number == seq2_y_number:
                grid[y_index].append(previous_number+1)
            else:
                grid[y_index].append(previous_number)

        print(f'newly appended grid: {grid}')
    return grid

print(starter_grid_x([2,7,8,3], [5,2,8,7,3]))

def starter_grid(sequence1_x, sequence2_y):
    grid = starter_grid_x(sequence1_x, sequence2_y)

    x_index = 0
    for y_index in range(1, len(sequence2_y)):
        seq2_y_number = sequence2_y[y_index]
        print('\n------------------\n')
        print(f'x_index: {x_index}, y_index: {y_index}')
        print(f'grid: {grid}')

        seq1_x_number = sequence1_x[x_index]
        previous_number = grid[y_index-1][x_index]

        print(f'\nx and y index are not 0')
        print(f'seq1_x_number: {seq1_x_number}, seq2_y_number: {seq2_y_number}')
        print(f'previous_number: {previous_number}')
        print(f'\ngrid: {grid}')

        if seq1_x_number == seq2_y_number:
            grid.append([previous_number+1])
        else:
            grid.append([previous_number])

        print(f'newly appended grid: {grid}')

    return grid

print(starter_grid([2,7,8,3], [5,2,8,7,3]))
# print(starter_grid([5,2,8,7,3], [2,7,8,3]))

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
