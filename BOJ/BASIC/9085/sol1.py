import sys
sys.stdin = open('input.txt')

for _ in range(int(input())):
    input()
    print(sum(map(int, input().split())))