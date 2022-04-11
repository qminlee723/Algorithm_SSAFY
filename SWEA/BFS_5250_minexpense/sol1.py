from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(i, j):
    distance[i][j] = 0
    Q = deque()
    Q.append(i, j)

    while Q:
        x, y = Q.popleft()

        for k in range(4):


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    route = [list(map(int, input().split())) for _ in range(N)]

    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(f'#{tc} {bfs(0, 0)}')