# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    sorted_points = sorted(segments, key=lambda segment: segment.start)

    print('\n-----------------------')
    print(f'sorted points: {sorted_points}')
    print('-----------------------\n')

    points = []
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

optimal_points([Segment(2,5), Segment(1,3), Segment(3,6)])

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     print(len(points))
#     for p in points:
#         print(p, end=' ')
