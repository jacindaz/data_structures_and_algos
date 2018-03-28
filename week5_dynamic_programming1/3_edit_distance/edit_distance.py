# Uses python3
# import ipdb

# REMEMBER!!!
#  => smallest unit of work
#  => create methods for each unit of work, so you can test separately
#  => even if you're not sure if it'll work, just write it and try
#      (to avoid getting stuck in a loop)
def iteration_printing(char1, char2, string1_edits, string2_edits, string1_index, string2_index):
    print(f'\nchar1: {char1}, char2: {char2}')
    print(f'string1_edits: {string1_edits}, string2_edits: {string2_edits}')
    print(f'string1_index: {string1_index}, string2_index: {string2_index}')

def starter_edit_distances(string1, string2):
    edit_distances = [list(range(0,len(string1)+1))]

    for index in range(1,len(string2)+1):
        edit_distances.append([index])

    return edit_distances

# print(starter_edit_distances('short', 'ports'))
# [[0, 1, 2, 3, 4, 5], [1], [2], [3], [4], [5]]

def edit_distance(string1, string2):
    if string1 == string2:
        return 0

    results = starter_edit_distances(string1, string2)
    string1_index = 0
    string2_index = 0

    for string1_index, char1 in enumerate(string1):
        for string2_index, char2 in enumerate(string2):
            char1 = string1[string1_index]
            char2 = string2[string2_index]

            print(f'\nstring1: {string1}, string2: {string2}')
            print(f'char1: {char1}, char2: {char2}')
            print(f'string1_index: {string1_index}, string2_index: {string2_index}')

            corner_point = results[string2_index][string1_index]
            point_above = results[string2_index][string1_index+1]
            point_left = results[string2_index+1][string1_index]
            min_distance = min(corner_point, point_above, point_left)

            if char1 != char2:
                results[string2_index+1].append(min_distance+1)
            else:
                if min_distance == corner_point:
                    results[string2_index+1].append(min_distance)
                elif min_distance == point_above:
                    results[string2_index+1].append(min_distance+1)
                elif min_distance == point_left:
                    results[string2_index+1].append(min_distance+1)

            print(f'\ncorner_point: {corner_point}, point_above: {point_above}, point_left: {point_left}')
            print(f'min distance: {min_distance}')
            print(f'results: {results}')

    return results

expected_result = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 2, 3, 4, 5, 6, 7, 7], [2, 1, 2, 3, 4, 5, 6, 7, 8], [3, 2, 1, 2, 3, 4, 5, 6, 7], [4, 3, 2, 2, 2, 3, 4, 5, 6], [5, 4, 3, 3, 3, 3, 4, 5, 6], [6, 5, 4, 4, 4, 4, 3, 4, 5], [7, 6, 5, 5, 5, 5, 4, 4, 5]]
actual_result = edit_distance('distance', 'editing')
print(f'expected_result: {expected_result}')
print(f'actual_result: {actual_result}')
print(f'does expected == actual? {expected_result == actual_result}')

# print(edit_distance('short', 'ports')) # 3
# print(edit_distance('roar', 'boar'))
# print(edit_distance('ello', 'hello'))
# print(edit_distance('hello', 'ello'))


# Input:
# ab
# ab
# Output: 0

# Input:
# short
# ports
# Output: 3

# Input:
# editing
# distance
# Output: 5


# [
#     [0, 1, 2, 3, 4, 5],
#     [1, 1, 2, 3, 4, 5],
#     [2, 2, 2, 2, 3, 4],
#     [3, 3, 3, 3, 2, 3],
#     [4, 4, 4, 4, 3, 2],
#     [5, 4, 5, 5, 4, 3]
# ]

# editing distance
# [
#     [0, 1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 1, 2, 3, 4, 5, 6, 7, 7],
#     [2, 1, 2, 3, 4, 5, 6, 7, 8],
#     [3, 2, 1, 2, 3, 4, 5, 6, 7],
#     [4, 3, 2, 2, 2, 3, 4, 5, 6],
#     [5, 4, 2, 3, 3, 3, 4, 5, 6],
#     [6, 5, 3, 3, 4, 4, 3, 4, 5],
#     [7, 6, 4, 4, 4, 5, 4, 4, 5]
# ]
