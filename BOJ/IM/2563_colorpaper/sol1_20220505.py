import sys
sys.stdin = open('input.txt')

N = int(input())
drawing_paper = [[0] * 100 for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())

    # 빈 도화지를 돌면서 x, y를 왼쪽 꼭지점으로 가지는 색종이를 칠한다(1로 만든다)
    for i in range(10):
        for j in range(10):
            drawing_paper[x+i][y+j] = 1

cnt = 0
for k in drawing_paper:
    cnt += sum(k)

print(cnt)