import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(v):
    Q = deque()
    Q.append(v)

    visited[v[0]][v[1]] = 1

    while Q:
        w = Q.popleft()

        if w[0] == N - 1 and w[1] == M - 1:
            return visited[w[0]][w[1]]

        for i in range(4):
            ni = w[0] + di[i]
            nj = w[1] + dj[i]

            if 0 <= ni < N and 0 <= nj < M:

                if maze[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    visited[ni][nj] = visited[w[0]][w[1]] + 1
                    Q.append((ni,nj))


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

v = (0, 0)

print(bfs(v))