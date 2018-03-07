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

# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))

def fibonacci(n):
    if n == 0:
        return [0]
    else:
        results = [0, 1]
        index = 2

        for x in range(2,n+1):
            sum = results[index-1] + results[index-2]
            results.append(sum)
            index += 1

    return results

def find_pisano_period_length(fibonacci_num, mod):
    pisano_period = []
    pisano_period_length = 0
    num_times_seen_011 = 0

    index = 0
    while num_times_seen_011 < 2:
        if pisano_period == ['0', '1', '1']:
            num_times_seen_011 += 1

        if num_times_seen_011 == 2:
            break

        mod_result = fibonacci(index)[-1] % mod

        print('\n------------------')
        print(f'pisano_period: {pisano_period}, pisano_period_length: {pisano_period_length}')
        print(f'num_times_seen_011: {num_times_seen_011}')
        print(f'mod_result = fibonacci(index)[-1] % mod: {mod_result}')
        print('------------------\n')

        if len(pisano_period) == 3:
            pisano_period.append(str(mod_result))
            pisano_period = pisano_period[-3:]
        else:
            pisano_period.append(str(mod_result))

        pisano_period_length += 1
        index += 1

    pisano_period = pisano_period[0:-3]
    pisano_period_length -= 3

    return pisano_period_length

def fibonacci_huge(fibonacci_num, mod):
    pisano_length = find_pisano_period_length(fibonacci_num, mod)
    remainder = fibonacci_num % pisano_length
    fib_remainder = fibonacci(remainder)[-1]

    return fib_remainder % mod

# print(find_pisano_period_length(10, 3))
# print(fibonacci_huge(239, 1000))
# print(fibonacci_huge(2816213588, 30524)) # 10249
