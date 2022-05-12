import pprint
import sys
sys.stdin = open('input.txt')

# arr = [[0] * 1001 for _ in range(1001)]
arr = [[0] * 1001 for _ in range(1001)]
N = int(sys.stdin.readline())
for k in range(1, N+1):
    x, y, width, height = map(int, sys.stdin.readline().split())

    for i in range(x, x+width+1):
        for j in range(y, y+height+1):
            if x <= i < x + width and y <= j < y + height:
                arr[i][j] = k


for r in range(N):
    rlt = 0
    for c in arr:
        rlt += c.count(r+1)
    print(rlt)
