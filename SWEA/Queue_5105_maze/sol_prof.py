
def check(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N -1:


def maze(x, y):
    visited[x][y] = 1
    while Q:
        x, y = Q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check(nx, ny):
                if data[nx][ny] == 0 and




T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split()))]