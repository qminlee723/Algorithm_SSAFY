import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N):
        curr_value = 0
        for j in range(K):
            # 일단 범위
            if i + j < N:
                curr_value += arr[i][i+j]
        if max_value < curr_value:
            max_value = curr_value


    print(f'#{tc} {max_value}')