import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # s = 작업 시작 시간, e = 작업 종료 시간
    for _ in range(N):
        s, e = map(int, input().split())


