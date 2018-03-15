#Uses python3
import sys

def is_greater_or_equal(number, max_number):
    shortest_length = 0
    if len(str(number)) <= len(str(max_number)):
        shortest_length = len(str(number))
    else:
        shortest_length = len(str(max_number))

    truncated_number = int(str(number)[:shortest_length])
    truncated_max_number = int(str(max_number)[:shortest_length])

    if truncated_number >= truncated_max_number:
        return True
    else:
        return False

def largest_number(numbers):
    answer = ""
    while len(numbers) > 0:
        max_number = numbers[0]
        for number in numbers:
            if is_greater_or_equal(number, max_number):
                max_number = number

        answer += str(max_number)
        numbers.remove(max_number)

    return answer

print(largest_number([2,8,2,3,6,4,1,1,10,6,3,3,6,1,3,8,4,6,1,10,8,4,10,4,1,3,2,3,2,6,1,5,2,9,8,5,10,8,7,9,6,4,2,6,3,8,8,9,8,2,9,10,3,10,7,5,7,1,7,5,1,4,7,6,1,10,5,4,8,4,2,7,8,1,1,7,4,1,1,9,8,6,5,9,9,3,7,6,3,10,8,10,7,2,5,1,1,9,9,5]))
# 9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))
