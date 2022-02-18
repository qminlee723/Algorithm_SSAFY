#delta를 이용한 풀이

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    # 현재, 우, 하, 우하, 좌하, 좌, 좌상, 상, 우상
    d_row = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    d_col = [0, 1, 0, 1, -1, -1, -1, 0, 1]

    # 파리채가 2*2 일 때
    if M == 2:
        max_sum = 0
        # 파리판에서 파리채가 움직일 수 있는 최대 범위(N-M+1)
        for i in range(N-M+1):
            for j in range(N-M+1):
                summation = 0
                # 방향 4개를 돌면서 지나가는 값들을 더해준다
                for k in range(4):
                    n_row = i + d_row[k]
                    n_col = j + d_col[k]
                    summation += flies[n_row][n_col]
                # summation 이후 최대값
                if max_sum < summation:
                    max_sum = summation

    # 파리채가 3*3 일 때
    elif M == 3:
        max_sum = 0
        # 파리판에서 파리채가 움직일 수 있는 최대 범위
        # 단, 시작점은 (1,1)이어야 한다 (otherwise, 파리판 밖으로 나감).
        # 그래서 
        for i in range(1, N-M+2):
            for j in range(1, N-M+2):
                summation = 0
                # 방향 9개를 돌면서 지나가는 값들을 더해준다.
                for k in range(9):
                    n_row = i + d_row[k]
                    n_col = j + d_col[k]
                    summation += flies[n_row][n_col]
                # summation 이후 최대값
                if max_sum < summation:
                    max_sum = summation

    print(f'#{tc} {max_sum}')


