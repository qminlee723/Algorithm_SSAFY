import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    total_price = 0
    price = int(input())
    total_price += price
    n = int(input())
    for i in range(n):
        q, p = map(int, input().split())
        total_price += (q * p)

    print(total_price)

