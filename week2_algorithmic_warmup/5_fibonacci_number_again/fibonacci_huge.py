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

    for x in range(2,n):
        sum = results[index-1] + results[index-2]
        results.append(sum)
        index += 1

    return results

def blah(fibonacci_num, mod):
    # calculate period of n % m
    #  => since a new period always starts with 011
    #  => that's how we know that a period is complete
    # then look at length of the period
    # n/(length of period), remainder
    #
    # Example: 𝐹2015 mod 3
    # period for Fi mod 3 is length 8
    # 2015/8 => (251*8) + 7
    # 𝐹2015 mod 3 = 𝐹7 mod 3 = 1.
    #
    # (future optimization later):
    # keep track of length, don't need to store actual period

    # calculate fibonacci
    fibo = fibonacci(fibonacci_num)

    # calculate period of n % m
    # 𝐹𝑖 mod 2 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0
    pisano_period = []  # { }
    for f in fibo:
        mod_result = f % mod
        pisano_period.append(str(mod_result))

        print(f'\nmod_result: {mod_result} \t\tf: {f} \t\tmod: {mod}')
        print(f'pisano_period: {pisano_period}\n')

        # stop checking if period contains pattern "011"
        if (len(pisano_period) > 3 and pisano_period[-3:] == ['0', '1', '1']) == True:
            pisano_period = ''.join(pisano_period[0:-3])

            pdb.set_trace()
            break



# print(fibonacci(239))
print(blah(239, 5))
