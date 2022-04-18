import sys
sys.stdin = open('input.txt')

def prime(n):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for j in num_list:
    if prime(j):
        cnt += 1
print(cnt)
