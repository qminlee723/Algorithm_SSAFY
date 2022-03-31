import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(start):
    Q = deque()
    Q.append(1)

    while Q:
        w = Q.popleft()

        for i in range(m):
            if famtree[i][0] == w:
                visited[i] += visited[w] + 1
                Q.append(famtree[i][1])
    return visited[w]

n = int(input())
# a와 b 사이의 촌수 계산
start, end = map(int, input().split())
m = int(input())
famtree = [list(map(int, input().split())) for _ in range(m)]
visited = [0] * (m+1)

print(bfs(start))