# import sys
# from collections import deque
#
# sys.stdin = open('input.txt')
#
# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#
#     while queue:
#         v = queue.popleft()
#
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#
# n, m = map(int, input().split())
#
# graph = []
# visited = True
# for i in range(m):
#     graph.append(list(map(int, input().split())))
#
# print(bfs(graph, 1, visited))
#
#

from collections import deque, defaultdict
import sys

sys.stdin = open('input.txt')


n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    count = 1
    queue = deque([start])
    visited = [False]*(n+1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
                count += 1
    return count


result = []
max_count = 0
for i in range(1, n+1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(*result)