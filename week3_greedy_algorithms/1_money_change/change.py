# Uses python3
import sys

def get_change(money):
    total_coins = 0

    for coin in [10, 5, 1]:
        if money/coin >= 1:
            num_tens = money//coin
            total_coins += num_tens
            money -= num_tens*coin

    return total_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
