#Uses python3
import sys
import math
# import collections

'''
    Task:
    Find 2 points whose distance is the shortest
    amongst a list of points.
'''

def naive_minimum_distance(x_coords, y_coords):
    points = []
    for i in range(len(x_coords)):
        points.append((x_coords[i], y_coords[i]))
    print(f'points: {points}')

    sort_by_x = sorted(points, key=lambda point: point[0])
    print(f'sort_by_x: {sort_by_x}')

    minimum_distance = float("inf")
    index = 0
    while index < len(sort_by_x)-2:
        point1 = sort_by_x[index]
        point2 = sort_by_x[index+1]
        x = (point1[0] - point2[0]) ** 2
        y = (point1[1] - point2[1]) ** 2
        distance = (x + y) ** (1/2)

        if distance < minimum_distance:
            minimum_distance = distance
            min_distance_pts = [point1, point2]
        index += 1

    print(f'\nminimum_distance: {minimum_distance}')
    print(f'min_distance_pts: {min_distance_pts}\n')

    return minimum_distance

# print(naive_minimum_distance([7,1,4,7], [7,100,8,7]))

def fast_minimum_distance(x_coords, y_coords):
    # naive algorithm:
    #  => keep track of minimum distance
    #  => O(n^2)
    #  => multiple every x and y coordinate
    print(f'x_coords: {x_coords}, y_coords: {y_coords}')

    # change to points
    points = []
    for i in range(len(x_coords)):
        points.append((x_coords[i], y_coords[i]))
    print(f'points: {points}')

    sort_by_x = sorted(points, key=lambda point: point[0])
    print(f'sort_by_x: {sort_by_x}')

    # construct points, using a python collection
    # points_map = collections.defaultdict(set)
    # sort by x coordinates
    # sort by y coordinates

    print(f'\nminimum_distance: {minimum_distance}')
    print(f'min_distance_pts: {min_distance_pts}\n')

    return minimum_distance

print(minimum_distance([7,1,4,7], [7,100,8,7]))


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     x = data[1::2]
#     y = data[2::2]
#     print(minimum_distance(x,y))
    # print("{0:.9f}".format(minimum_distance(x, y)))

# Input:
# 2
# 0 0
# 3 4
# Output:
# 5.0


# Input:
# 4
# 7 7
# 1 100
# 4 8
# 7 7
# Output:
# 0.0
