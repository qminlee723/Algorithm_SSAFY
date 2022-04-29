import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M +1):

            curr_kill = 0
            for r in range(M):
                for c in range(M):
                    curr_kill += arr[r+i][c+j]

            if max_kill < curr_kill:
                max_kill = curr_kill

    print(f'#{tc} {max_kill}')