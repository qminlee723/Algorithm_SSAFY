import sys; sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())  #정점수
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    ch = [0] * (N + 1)

    for _ in range(N):
        # arr = [부모번호, 알파벳, 왼쪽, 오른쪽]
        arr = input().split() # 문자열의 리스트로
        p = int(arr[0])
        ch[p] = arr[1]
        if len(arr) >= 3:  # 왼쪽 자식이 있는 경우
            L[p] = int(arr[2])
        if len(arr) == 4:   # 오른쪽 자식이 있는 경우
            R[p] = int(arr[3])

    def inorder(v):
        if v == 0:
            return
        inorder(L[v])
        print(ch[v], end='')
        inorder(R[v])

    print(f'#{tc} ',end='')
    inorder(1)
    print()