import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(start):
    Q = deque()
    Q.append(start)
    visited[start] = 1

    while Q:
        node = Q.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] += visited[node] + 1
                Q.append(i)

n = int(input())
# a와 b 사이의 촌수 계산
start, end = map(int, input().split())
# 부모자식간 관계의 갯수
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for _ in range(m):
    x, y = map(int, input().split())
    # 그래프의 인덱스를 노드 숫자로 하고, append 값은 연결된 노드로 이어지게 그래프에 저장
    graph[x].append(y)
    graph[y].append(x)

bfs(start)

if visited[end] != 0:
    print(visited[end]-1)
else:
    print(-1)