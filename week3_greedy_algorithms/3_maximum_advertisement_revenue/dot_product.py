#Uses python3
import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

def greedy_dot_product(profit_per_click, avg_clicks):
    profit_per_click = sorted(profit_per_click, reverse=True)
    avg_clicks = sorted(avg_clicks, reverse=True)

    products = []
    for index, click in enumerate(profit_per_click):
        products.append(click * avg_clicks[index])

    products = sorted(products, reverse=True)
    return sum(products)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(bananas(a, b))
