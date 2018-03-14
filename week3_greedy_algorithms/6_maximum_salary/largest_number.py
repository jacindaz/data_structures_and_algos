#Uses python3
import sys

# Interestingly, for solving this problem, you need to
# replace the check digit >= maxDigit with a call
# IsGreaterOrEqual(digit, maxDigit) for an appropriately
# implemented function IsGreaterOrEqual.
# For example, IsGreaterOrEqual(2, 21) should return True.
def largest_number(numbers):
    answer = ""
    while len(numbers) > 0:
        max_digit = float("-inf")

        print('\n------------------------------')

        for number in numbers:
            print(f'number: {number}, numbers: {numbers}')
            print(f'max digit: {max_digit}, answer: {answer}')

            if number >= max_digit:
                max_digit = number
                print(f'new max digit: {max_digit}')

        answer += str(max_digit)
        numbers.remove(max_digit)

        print(f'appended to answer: {answer}, removed a number: {numbers}')
        print('------------------------------\n')

    return answer

# print(largest_number([9,4,6,1,9]))
# 5
# 9 4 6 1 9
# Output:
# 99641

# print(largest_number([23, 39, 92]))
# 3
# 23 39 92
# Output:
# 923923

print(largest_number([21, 2]))
# 2
# 21 2
# Output:
# 221

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))

