import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and 

    return

def bfs(v):
    visited = []
    Q = deque()
    Q.append(v)

    while Q:
        w = Q.popleft()
        if w not in visit:

    return

N, M, V = map(int, input().split())
nodes = []
graph = {}

for i in range(M):
    a, b = map(int, input().split())


    print(dfs(v))
    print(bfs(v))