# Uses python3
import sys
import pdb

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def print_things(remainder, pisano_1, pisano_2, pisano_period_length, fib_1, fib_2):
    print('\n------------------------------')
    print(f'remainder: {remainder}')
    print(f'pisano_1: {pisano_1}, pisano_2: {pisano_2}')
    print(f'pisano_period_length: {pisano_period_length}\n\n')
    print(f'fib_1: {fib_1}, fib_2: {fib_2}')
    print('------------------------------\n')

def find_pisano_period_length(mod):
    pisano_1 = '0'
    pisano_2 = '0'
    fib_1 = 0
    fib_2 = 1
    pisano_length = 0

    done = False

    while done == False:
        if (pisano_1 == '0' and pisano_2 == '1') == True:
            done = True
            pisano_length -= 1
        else:
            remainder = fib_1 % mod
            pisano_2 = pisano_1
            pisano_1 = str(remainder)

            pisano_length += 1

            new_fib = fib_1 + fib_2
            fib_2 = fib_1
            fib_1 = new_fib

            print_things(remainder, pisano_1, pisano_2, pisano_length, fib_1, fib_2)

    return pisano_length

# print(find_pisano_period_length(3)) # 8
# print(find_pisano_period_length(1975)) # 3900


def fibonacci_huge(fibonacci_num, mod):
    pisano_length = find_pisano_period_length(fibonacci_num, mod)

    remainder = fibonacci_num % pisano_length
    fib_remainder = fibonacci(remainder)[-1]

    return fib_remainder % mod

# print(find_pisano_period_length(10, 3)) # 1
# print(fibonacci_huge(10, 3))
# print(fibonacci_huge(239, 1000)) # 161
# print(fibonacci_huge(2816213588, 30524)) # 10249

# print(find_pisano_period_length(100, 100000))
# print(fibonacci_huge(100, 100000)) #

# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(fibonacci_huge(n, m))
