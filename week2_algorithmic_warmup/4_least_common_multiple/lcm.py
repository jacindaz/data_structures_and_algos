# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

def euclidean(a,b):
    if b == 0:
        return a

    remainder = float(a) % float(b)
    return euclidean(b, remainder)

def lcm(a,b):
    gcd = euclidean(a,b)
    return (a*b)/gcd

# lcm_naive(28851538, 1183019)
lcm(28851538, 1183019)
# euclidean(28851538,1183019)

