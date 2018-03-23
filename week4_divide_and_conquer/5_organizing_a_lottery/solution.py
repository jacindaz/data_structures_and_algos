import collections

def fast_count_segments(starts, ends, points):
    left_label, point_label, right_label = (1, 2, 3)
    count = [0] * len(points)

    # Regular dict object cannot be used here, because points are not unique.
    points_map = collections.defaultdict(set)

    pairs = []
    for i in starts:
        pairs.append((i, left_label))
    print(f'\nappended starts and left_label. left_label: {left_label}, starts: {starts}')
    print(f'pairs: {pairs}\n')

    for i in ends:
        pairs.append((i, right_label))
    print(f'\nappended ends and right_label. right_label: {right_label}, ends: {ends}')
    print(f'pairs: {pairs}\n')

    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        points_map[point].add(i)
    print('\nappending points')
    print(f'points: {points}')
    print(f'pairs: {pairs}')
    print(f'points_map: {points_map}')

    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))

    coverage = 0
    for pair in sorted_pairs:
        print(f'\n-----------------------------\n')
        # print(f'left_label: {left_label}, right_label: {right_label}, point_label: {point_label}')
        print(f'pair: {pair}, pair[1]: {pair[1]}, coverage: {coverage}')

        if pair[1] == left_label:
            coverage += 1
            print(f'pair[1] == left_label, coverage is now: {coverage}')
        if pair[1] == right_label:
            coverage -= 1
            print(f'pair[1] == right_label, coverage is now: {coverage}')
        if pair[1] == point_label:
            # points_map keeps track of which indices in the
            # count list is for which point
            # need this in case there are duplicate points,
            # which will have different indices
            indices = points_map[pair[0]]
            print(f'pair[1] == point_label, coverage is now: {coverage}')
            print(f'indices is now: {indices}')

            for i in indices:
                count[i] = coverage
                print(f'i: {i}, count: {count}, coverage: {coverage}')

    return count

print(fast_count_segments([0, 7], [5, 10], [1, 6, 11]))
# [1, 0, 0]
# print(fast_count_segments([-10], [10], [-100, 100, 0]))
# [0, 0, 1]
# print(fast_count_segments([0, -3, 7], [5, 2, 10], [1, 6]))
# [2, 0]
# print(fast_count_segments([0, 2, 4], [5, 2, 10], [1, 6, 2, 2]))
# [1, 1, 2, 2]
