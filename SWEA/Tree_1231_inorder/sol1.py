import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    ch = [0] * (N + 1)

for _ in range(N):
    # arr = [부모번호, 알파벳, 왼쪽, 오른쪽]
    arr = input().split()
    p = int(arr[0])
    ch[p] = arr[1]
    if len(arr) >= 3:       # 왼쪽 자식이 있는 경우
        L[p] = int(arr[2])
    if len(arr) == 4:       # 오른쪽 자식이 있는 경우
        R[p] = int(arr[3])

    def in_order(v):
        if v == 0:
            return
        in_order(L[v])
        print(ch[v], end='')
        in_order(R[v])

    print(f'#{tc}', end='')
    in_order(1)
    print()


    for i in range(0, N * 2, 2):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c



    print(arr)
# print(f'#{tc} {ans}')