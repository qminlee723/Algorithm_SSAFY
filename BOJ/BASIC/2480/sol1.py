import sys
sys.stdin = open('input.txt')

a, b, c = map(int, input().split())


if a == b == c:
    print(10000 + a * 1000)
elif a != b and b != c and a != c:
    max_num = max(a, b, c)
    print(max_num * 100)
else:
    if a == b or a == c:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)

