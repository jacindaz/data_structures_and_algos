# Uses python3

n = int(input())
a = [int(x) for x in input().split()]

largest_number = a[0]
second_largest = a[0]


if len(a) == 2:
    print(largest_number*second_largest)
else:
    for i in a:
        if i > largest_number:
            largest_number = i

    for i in a:
        if i == largest_number:
            pass
        elif i > second_largest:
            second_largest = i

    print(largest_number*second_largest)
