# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    sorted_segments = sorted(segments, key=lambda segment: segment.end)
    points = []

    while len(sorted_segments) > 0:
        segment = sorted_segments[0]
        min_right_endpoint = segment.end
        points.append(min_right_endpoint)

        print(f'\nsorted_segments: {sorted_segments}')
        print(f'segment: {segment}')
        print(f'min_right_endpoint: {min_right_endpoint}, points: {points}')

        inner_index = 0
        while inner_index < len(sorted_segments):
            current_segment = sorted_segments[inner_index]
            if min_right_endpoint in range(current_segment.start, current_segment.end+1):
                print(f'deleting segment: {current_segment}')
                sorted_segments.remove(current_segment)
            else:
                inner_index += 1

    return points


# print(optimal_points([Segment(1,3), Segment(2,5), Segment(3,6)]))
# 1
# 3

# print(optimal_points([Segment(4,7), Segment(1,3), Segment(2,5), Segment(5,6)]))
# 3 6


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *data = map(int, input.split())
#     segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     points = optimal_points(segments)
#     print(len(points))
#     for p in points:
#         print(p, end=' ')
