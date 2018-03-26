# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

# result = list(optimal_sequence(96234))
# result = list(optimal_sequence(6))
# print(len(result)-1) # 15
# for x in result:
#     print(x, end=' ')

# REMEMBER!!!
#  => smallest unit of work
#  => create methods for each unit of work, so you can test separately
#  => even if you're not sure if it'll work, just write it and try
#      (to avoid getting stuck in a loop)
#
def dp_starter_sequence():
    results = [[0], [1]]
    for i in range(2,7):
        result = list(optimal_sequence(i))
        results.append(result)
    return results

# print(dp_starter_sequence())

def dp_sequence(number):
    # starter results: [[0], [1], [1, 2], [1, 3], [1, 2, 4], [1, 2, 4, 5], [1, 2, 6]]
    # for n: 0-6
    results = dp_starter_sequence()
    num_starter_results = len(results)-1

    # actions you're able to take:
    #  => multiply by 2
    #  => multiply by 3
    #  => add 1

    if number <= num_starter_results:
        return results[:number+1]
    else:
        for i in range(num_starter_results+1,number+1):
            result_min_ops = []
            min_operations = float('inf')

            if i % 3 == 0:
                starter_result_index = i // 3 # 4
                starter_result = results[starter_result_index] # [1,2,4]

                new_result = starter_result + [starter_result_index * 3]
                new_result_len = len(new_result)-1

                result_min_ops = new_result
                min_operations = new_result_len

            if i % 2 == 0:
                starter_result_index = i // 2 # 4
                starter_result = results[starter_result_index] # [1,2,4]

                new_result = starter_result + [starter_result_index * 2]
                new_result_len = len(new_result)-1

                if new_result_len < min_operations:
                    result_min_ops = new_result
                    min_operations = new_result_len

            # last check
            prior_result = results[-1]
            last_num_in_prior_result = prior_result[-1]

            new_result = prior_result + [last_num_in_prior_result + 1]
            new_result_len = len(new_result)-1

            if new_result_len < min_operations:
                result_min_ops = new_result
                min_operations = new_result_len

            results.append(result_min_ops)

    return results

# for n in range(1,20):
#     result = dp_sequence(n)[-1]
#     print(f'n: {n} \t\t{result} \t\tnum operations: {len(result)-1}')

# n = 96234
# result = dp_sequence(n)[-1]
# print(f'n: {n} \nresults: {result} \nnum operations: {len(result)-1}')
# both are correct answers:
# => 1 2 4 5
# => 1 3 4 5
# => num operations: 3

# 96234
# Output:
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234


input = sys.stdin.read()
n = int(input)
sequence = list(dp_sequence(n))[-1]
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

