import sys


def my_max(lst):
    max_v = 0
    for i in lst:
        if max_v < i:
            max_v = i
    return max_v

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price_list = list(map(int, input().split()))

    purchase_p = 0
    quantity = 0
    for i in range(len(price_list)):
        if price_list.index(my_max(price_list)) > i:
            quantity += 1
            purchase_p += price_list[i]
        else:
            print(0)
            break
    rlt = (my_max(price_list) * quantity) - purchase_p
    print(f'{tc} {rlt}')
