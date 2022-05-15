import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr1 = list(zip(*arr[::-1]))
    arr2 = list(zip(*arr1[::-1]))
    arr3 = list(zip(*arr2[::-1]))

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr1[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr2[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr3[i][j], end='')
        print(end=' ')
        print()

