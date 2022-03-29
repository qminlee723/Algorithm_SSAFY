import sys

sys.stdin = open('input.txt')

wid, len = map(int, input().split())
t_map = [list(input()) for _ in range(wid)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

