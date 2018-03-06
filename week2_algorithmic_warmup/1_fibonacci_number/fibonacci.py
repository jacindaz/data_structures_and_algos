# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fibonacci(n):
    if n == 0:
        return 0
    else:
        results = [0, 1]
        index = 2

        for x in range(2,n+1):
            sum = results[index-1] + results[index-2]
            results.append(sum)
            index += 1

    return results[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci(n))
