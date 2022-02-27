import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, p = map(int, input().split())
    arr = [list(input().split()) for _ in range(n)]
