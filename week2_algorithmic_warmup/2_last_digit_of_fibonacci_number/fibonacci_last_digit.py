# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def better_solution(n):
    results = [1]
    index = 1

    for x in range(2,n):
        sum = (results[index-1] + results[index-2]) % 10
        results.append(sum)
        index += 1

    return results[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(better_solution(n))
