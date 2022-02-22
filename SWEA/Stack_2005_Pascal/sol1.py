import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (N) for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            # 만약 위치가 arr의 양 끝이라면 1을
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
            # 위치가 arr 중간이라면 위의 값들의 합을 받는다

    print(f'#{tc}')
    for a in arr:
        print(*arr[i])
