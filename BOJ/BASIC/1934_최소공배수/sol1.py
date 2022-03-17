import sys
sys.stdin = open('input.txt')

T = int(input())

def cal(a, b):
    A, B = a, b
    while a % b == 0:
        a, b = b, a % b
    return ((A * B) // b)

for _ in range(T):
    A, B = map(int, input().split())
    print(cal(A, B))

