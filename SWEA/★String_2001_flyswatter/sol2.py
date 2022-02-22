# for 문을 이용한 풀이

import sys
from pprint import pprint

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):

    # 입력 받기
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for r in range(N - M + 1):
        for c in range(N - M  + 1):

            curr_kill = 0
            for i in range(M):
                for j in range(M):
                    curr_kill += flies[r + i][c + j]  # 파리 계산

            if max_kill < curr_kill:
                max_kill = curr_kill

    print(f"#{tc} {max_kill}")






# import sys
# from pprint import pprint
#
# sys.stdin = open("input.txt")
#
# T = int(input())
# for tc in range(1, T + 1):
#
#     # 입력 받기
#     N, M = map(int, input().split())
#     flies = [list(map(int, input().split())) for _ in range(N)]
#
#     max_kill = 0
#     for r in range(N - M + 1):
#         for c in range(N - M  + 1):
#
#             curr_kill = 0
#             for i in range(M):
#                 for j in range(M):
#                     curr_kill += flies[r + i][c + j]  # 파리 계산
#
#             if max_kill < curr_kill:
#                 max_kill = curr_kill
#
#     print(f"#{tc} {max_kill}")


