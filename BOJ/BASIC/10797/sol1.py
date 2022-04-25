import sys
sys.stdin = open('input.txt')

n = int(input())
lst = map(int, input().split())

cnt = 0
for i in lst:
    if i == n:
        cnt += 1

print(cnt)