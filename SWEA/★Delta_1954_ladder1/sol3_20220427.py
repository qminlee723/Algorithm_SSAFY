import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착점에서 올라가야 출발점을 알수 있으니 도착점 먼저 찾기
    for j in range(100):
        if arr[99][j] == 2:
            break
    i = 99
    # i, j 구해서 도착점 좌표 알 수 있음

    while i > 0:
        i -= 1
        # 1이 길이니까 1이 이어지는동안 계속 가야됨
        if 0 < j and arr[i][j-1] == 1:
            while 0 < j and arr[i][j-1] == 1:
                j -= 1
        elif j < 99 and arr[i][j+1] == 1:
            while j < 99 and arr[i][j+1] == 1:
                j += 1

    print(f'#{tc} {j}')










