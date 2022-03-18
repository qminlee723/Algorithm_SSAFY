import sys
sys.stdin = open('input.txt')

for i in range(3):
    a, b = list(map(int, input().split()))
    print(a, b)
