n = int(input())
a = [int(x) for x in input().split()]

largest_number = 0
second_largest = 0

print(f'n: {n} \ta: {a}')

for i in a:
    if i > largest_number:
        print(f'i: {i} \tlargest_number: {largest_number}')
        largest_number = i

print('\n')
for i in a:
    if i == largest_number:
        print(f'i: {i} \tlargest_number: {largest_number}')
        pass
    elif i > second_largest:
        print(f'i: {i}, second_largest: {second_largest} \tlargest_number: {largest_number}')
        second_largest = i

print(largest_number*second_largest)
