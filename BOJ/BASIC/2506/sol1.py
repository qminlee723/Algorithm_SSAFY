import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))

ans = 0
total_score = 0
for i in range(N):
    if lst[i] == 0:
        total_score = 0
    elif lst[i] == 1:
        total_score += 1
    ans += total_score

print(ans)