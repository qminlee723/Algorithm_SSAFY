import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())

lst = []
for i in range(N):
    if M <= i**2 <= N:
        lst.append(i**2)
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))



