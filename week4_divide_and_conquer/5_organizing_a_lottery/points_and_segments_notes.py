# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    #write your code here
    return count

def naive_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):

            print('\n-----------------------\n')
            print(f'i: {i}, j: {j}, count: {count}')
            print(f'starts[j]: {starts[j]}, points[i]: {points[i]}, ends[j]: {ends[j]}')
            print(f'points: {points}')

            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count

print(naive_count_segments([0,7],[5,10],[1,6,11]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    count = naive_count_segments(starts, ends, points)
    for x in count:
        print(x, end=' ')


# Input:
# 2 3
# 0 5
# 7 10
# 1 6 11
# Output:
# 1 0 0
