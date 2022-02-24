import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    labyrinth = [list(map(int, input())) for _ in range(n)]

    # 출발점 찾기 (labyrinth 마지막 행에서 2인 곳)
    for j in range(n):
        if labyrinth[-1][j] == 2:
            break
    i = n

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = []
    result = 0


def DFS(graph, v, visited):
    visited[v]: True
    print(v, end='')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)



def dfs():

    queue = [[start[0]]]

    lst[x][y] = '2'
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < N and 0 <= new_y < N:

            if lst[new_x][new_y] == '3':
                result = 1
                return True

            elif lst[new_x][new_y] == '0':
                t = dfs(new_x, new_y)
                if t:
                    return True
        return False


visited = [[0] * N for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs():
    q = [[start[0]], start[1]]
    visited[start[0]][start[1]] = 1

    while q:
        r, c = q.pop()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < N and labyrinth[rr][cc] == 3:
                return True
            if 0 <= rr < N and 0 <= cc < N and labyrinth[rr][cc] == 0 and not visited[rr][cc]:
                q.append([rr, cc])
                visited[rr, cc] = 1

    return False