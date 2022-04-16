import sys
sys.stdin = open('input.txt')

odd = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        odd.append(num)
    else:
        continue

if len(odd) > 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)