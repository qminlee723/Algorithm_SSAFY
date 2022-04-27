import sys
sys.stdin = open('input.txt')

up, down, total = map(int, input().split())
cnt = 0
today = 0
while True:
    today += up
    if today >= total:
        break
    else:
        today -= down
        cnt += 1
print(cnt+1)