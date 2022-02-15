import sys
from pprint import pprint

sys.stdin = open('input.txt')

# T = int(input())
# n = int(input())
# matrix = []
# coo_red = []
# coo_blue = []
#
# for tc in range(n):
#     lst = list(map(int, input().split()))
#     if lst[-1] == 1:
#         coo_red.extend(lst[tc])
#     else:
#         coo_blue.extend(lst[tc])
#




T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data_set = [list(map(int, input().split())) for _ in range(n)]

    # 미리 set을 정의
    red = set()
    blue = set()
    for data in data_set:
        r1, c1, r2, c2, color = data

        # 각각의 범위에서 좌표를 구해서, set에 담는다

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):   # 범위는 항상 조심!
                if color == 1:
                    red.add((r, c))
                else:
                    blue.add((r, c))
    rlt = len(red & blue)
    print(f'#{tc} {rlt}')
