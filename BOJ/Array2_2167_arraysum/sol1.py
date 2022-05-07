import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())

