import sys
sys.stdin = open('input_hws.txt')

from collections import deque
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())

# 각 노드가 연결된 정보를 2차원 배열로 표현
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1


visited = [0] * (n + 1)
print(dfs(graph, v, visited))
