from collections import deque
import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x, y):
    queue = deque([x, y])
    visited =
    visited[x, y] = True

    while queue:
        x, y = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
                count += 1
    return count


result = []
for i in range(1, n+1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(*result)

from collections import deque


def bfs(x, y)
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] == graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m -1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))