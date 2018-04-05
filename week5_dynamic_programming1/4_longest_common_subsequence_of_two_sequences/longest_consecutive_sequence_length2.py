#Uses python3

import sys

def find_sequences(sequence):
    sub_sequences = []

    for index, number in enumerate(sequence):
        next_num_index = index+1

        while next_num_index < len(sequence):
            next_number = sequence[next_num_index]
            sub_sequences.append([number, next_number])
            next_num_index += 1

    return sub_sequences

# print(find_sequences([2,7,8,3]))

def lcs2(sequence1, sequence2):
    sub_sequences1 = find_sequences(sequence1)
    sub_sequences2 = find_sequences(sequence2)

    sub_sequences1 = sorted(sub_sequences1, key=lambda sub_seq: (sub_seq[0],sub_seq[1]))
    sub_sequences2 = sorted(sub_sequences2, key=lambda sub_seq: (sub_seq[0],sub_seq[1]))

    num_common_sub_sequence = 0
    for sub_seq1 in sub_sequences1:
        for sub_seq2 in sub_sequences2:
            if sub_seq1 == sub_seq2:
                # print(f'sub_seq1: {sub_seq1}, sub_seq2: {sub_seq2}')
                num_common_sub_sequence += 1

    return num_common_sub_sequence

# print(lcs2([7], [1,2,3,4])) # 0
# print(lcs2([2,7,8,3], [5,2,8,7])) # 2
# print(lcs2([2,7,5], [2,5])) # 2
# print(lcs2([1,2,3], [3,2,1])) # 1


# print(lcs([1,2,3], [1,2,3,4])) # 3
# print(lcs([-4,1,2,3], [1,2,3,-4])) # 3
