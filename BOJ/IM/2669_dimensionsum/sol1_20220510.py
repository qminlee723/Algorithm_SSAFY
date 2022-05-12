import sys
sys.stdin = open('input.txt')

graph = [[0]*100 for _ in range(100)]


for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if graph[r][c] == 1:
            cnt += 1

print(cnt)
