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
    results = [0, 1]
    index = 2

    for x in range(2,n+1):
        sum = results[index-1] + results[index-2]
        results.append(sum)
        index += 1

    return results

def find_pisano_period(fibonacci_num, mod):
    fibo = fibonacci(fibonacci_num)
    pisano_period = []
    for f in fibo:
        mod_result = f % mod
        pisano_period.append(str(mod_result))

        if (len(pisano_period) > 3 and pisano_period[-3:] == ['0', '1', '1']) == True:
            pisano_period = pisano_period[0:-3]
            break

    return pisano_period

def fibonacci_huge(fibonacci_num, mod):
    remainder = fibonacci_num % len(find_pisano_period(fibonacci_num, mod))
    return int(find_pisano_period(remainder, mod)[-1])
