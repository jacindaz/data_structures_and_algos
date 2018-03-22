# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    #write your code here
    return count

# print(fast_count_segments([0,7],[5,10],[1,6,11]))

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

# print(naive_count_segments([0,7],[5,10],[1,6,11]))
print(naive_count_segments([0,5],[5,10],[1,5,11]))



# Input:
# 2 3
# 0 5
# 7 10
# 1 6 11
# Output:
# 1 0 0
