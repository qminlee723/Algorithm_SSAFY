import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = map(int, input().split())
