# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fibonacci(n):
    results = [0, 1]
    index = 2

    for x in range(2,n):
        print(f'\nn: {n}\t\t results[index-1]: {results[index-1]}\t\t results[index-2]: {results[index-2]}')

        sum = results[index-1] + results[index-2]
        print(f'sum: {sum} \t\tresults: {results}')

        results.append(sum)
        index += 1

fibonacci(7)
