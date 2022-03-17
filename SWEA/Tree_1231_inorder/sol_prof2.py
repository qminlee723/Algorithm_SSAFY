import sys

sys.stdin = open('input.txt')

def inorder(root):
    if root:
        inorder(int(TREE[root][1]))
        print(TREE[root][0], end='')
        inorder(int(TREE[root][2]))
T = 10
for tc in range(1, T + 1):
    N = int(input())
    TREE = [[0]*3 for _ in range(N+1)]
    for _ in range(N):
        lst = list(input().split())
        p = int(lst[0])
        TREE[p][0:len(lst)-1] = lst[1:len(lst)]

    print(f'#{tc} ', end='')
    inorder(1)
    print()
