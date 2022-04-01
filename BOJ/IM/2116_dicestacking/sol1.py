import sys
sys.stdin = open('input.txt')

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
