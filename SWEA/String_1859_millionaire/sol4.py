# 보충 교수님 풀이

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))

    max_value = price[-1]
    profit = 0
    for i in range(n - 2, -1, -1):
        # 현재가가 최고가보다 크다면 최고가 갱신
        if price[i] >= max_value:
            max_value = price[i]
            # 현재가가 최고가보다 작다면
            # 최고가 - 현재가 이익 누적시키기
        else:
            profit += max_value - price[i]

    print(f'#{0} {1}'.format(tc, profit))
