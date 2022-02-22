#delta를 이용한 풀이

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]


    # 현재, 오른쪽, 아래, 오른쪽 대각선 아래 순으로 탐색
    d_row = [0, 0, 1, 1]
    d_col = [0, 1, 0, 1]

    # 범위 설정
    # 인덱스를  i j  로 갖는 파리판에서 현재 -> 오른쪽 -> 오른쪽 아래 -> 오른쪽 대각선 아래를 순차적으로 탐색하고
    # 거쳐가는 인덱스가 가리키는 숫자들을 모두 더해준다.

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            summation = 0
            for k in range(4):
                n_row = i + d_row[k]
                n_col = j + d_col[k]

                summation += flies[n_row][n_col]

            if max_sum < summation:
                max_sum = summation




print(f'#{tc} {max_sum}')


