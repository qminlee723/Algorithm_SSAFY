import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            kill_fly = 0
            for k in range(M):
                for l in range(M):
                    kill_fly += area[i+k][j+l]

            if max_fly < kill_fly:
                max_fly = kill_fly

    print(f'#{tc} {max_fly}')