import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(start):
    Q = deque()
    for l in range(len(start_lst)):
        Q.append(start_lst[l])
    visited[start[0]][start[1]] = 0

    while Q:
        w = Q.popleft()

        for k in range(4):
            ni = w[0] + di[k]
            nj = w[1] + dj[k]

            # 새로운 방향이 범위 벗어나지 않게
            if 0 <= ni < N and 0 <= nj < M:
                if farm[ni][nj] == 0 and visited[ni][nj] == 0:
                    farm[ni][nj] = 1
                    visited[ni][nj] = visited[w[0]][w[1]] + 1
                    Q.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 0:
                return -1
    return visited[w[0]][w[1]]


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
start_lst = []
start = tuple()

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            start = (i, j)
            start_lst.append(start)
        else:
            continue
if start:
    print(bfs(start))
else:
    print(-1)