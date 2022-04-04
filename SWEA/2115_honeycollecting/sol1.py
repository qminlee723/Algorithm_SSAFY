import sys
sys.stdin = open('input.txt')
# 부분집합의 합

def

T = int(input())
for tc in range(1, T + 1):
    # N = 벌통 크기, M = 벌통 갯수,  C = 꿀 최대 양
    N, M, C = map(int, input().split())
    bucket = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 * N for _ in range(N)]


    bfs(v)
    print(bucket)