# Uses python3
import sys

def get_change(money):
    min_num_coins = [0]

    for m in range(1,money+1):
        min_num_coins.append(float('inf'))

        for coin in [1,3,4]:
            if m >= coin:
                print('\n---------------\n')
                print(f'm: {m}, coin: {coin}')

                num_coins = min_num_coins[m-coin] + 1

                print(f'num_coins: {num_coins}, min_num_coins: {min_num_coins}')

                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
                    print('num_coins < min_num_coins[m] is true! ')
                    print(f'num_coins: {num_coins}, min_num_coins: {min_num_coins}')


    return min_num_coins[-1]

print(get_change(5)) # 2
print(get_change(4)) # 1
# print(get_change(34)) # 9
# print(get_change(2)) # 2

# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))


# Input:
# 2
# Output:
# 2
# 2 = 1 + 1.

# Input:
# 34
# Output:
# 9
# 34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.
