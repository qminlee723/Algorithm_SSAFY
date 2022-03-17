import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    Yonsei = 0
    Korea = 0
    for _ in range(9):
        Y, K = map(int, input().split())
        Yonsei += Y
        Korea += K

    if Yonsei > Korea:
        print('Yonsei')
    elif Korea > Yonsei:
        print('Korea')
    else:
        print('Draw')