import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]

    for _ in range(M):
        r, c, direction, jump = map(int, input().split())


        while 0 <= r < N and 0 <= c < N:
            matrix[r][c] = 1

            nr = r + dr[direction] * jump
            nc = c + dc[direction] * jump

            if 0 <= nr < N and 0 <= nc < N:
                matrix[nr][nc] = 1

    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0:
                cnt += 1

    print(cnt)


# 9
# 12
# 22