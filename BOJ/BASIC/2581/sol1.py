import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())

lst = []
for num in range(M, N + 1):
    ssum = 1
    for i in range(2, num):
        if num % i == 0:
            ssum = 0
            break
    if ssum and num != 1:
       lst.append(num)

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)