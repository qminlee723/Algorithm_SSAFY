import sys

sys.stdin=open('input.txt')

# 경하님 풀이
t = int(input())
for num in range(1, t+1):
    n = int(input())

    result = [[0] * n for _ in range(n)]

    #우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    #현재 이동방향
    #0:우, 1:하, 2:좌, 3:상, dx/dy 인덱스와 대응
    move = 0

    x = 0
    y = 0
    for i in range(1, n ** 2 + 1):
        #방문한 위치를 0에서 i로 바꿈
        result[x][y] = i
        #현재 이동방향을 유지할 때 다음 도착지점이 범위를 벗어나거나, 이미 방문한 곳이라면 방향을 바꿔야함
        #이때 이미 방문한 곳인지의 여부는 다음 도착점의 값이 0인지여부를 통해서 알 수 있음
        #방향을 바꿔야 한다면 우 > 하 > 좌 > 상 순으로 바꾸고, 인덱스가 0~3에서 반복되므로 나머지 연산 활용
        if x + dx[move] >= n or y + dy[move] >= n or x + dx[move] < 0 or y + dy[move] < 0 or result[x+dx[move]][y+dy[move]] != 0:
            move = (move + 1) % 4
        x += dx[move]
        y += dy[move]

    print(f'#{num}')
    for i in range(n):
        for j in range(n):
            print(result[i][j], end=" ")
        print()