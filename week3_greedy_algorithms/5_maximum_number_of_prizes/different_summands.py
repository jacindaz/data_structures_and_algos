# Uses python3
import sys

def optimal_summands(number):
    summands = []
    for i in range(1, number+1):
        print(f'i: {i}, number: {number}')
        print(f'summands: {summands}\n')

        if i * 2 >= number: # is this the last number ?
            summands.append(number)
            break

        else:
            summands.append(i)
            number = number - i
            i = i +1

    return summands

print(optimal_summands(6))
# 3
# 1 2 3

# print(optimal_summands(8))
# 3
# 1 2 5

# print(optimal_summands(2))
# 1
# 2

# print(optimal_summands(4))
# 2
# 1 3

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     summands = optimal_summands(n)
#     print(len(summands))
#     for x in summands:
#         print(x, end=' ')
