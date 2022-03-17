import sys

sys.stdin = open('input.txt')

# 중위순회 순서로 찾기
# def inorder(node):
#     if node:
#         inorder(c1[node])
#         print(node)
#         inorder(c2[node])

# 트리를 생성해줍니다
for tc in range(1, 11):
    N = int(input())

    # 빈 배열 생성 (왼쪽 애, 오른쪽 애, 부모, 값)
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    tree = [0] * (N + 1)

    # 빈 배열 채워서 트리 만들기
    for i in range(N):
        lst = list(input().split())
        # print(lst)
        # 만약 연산자가 끼어있다면,
        if len(lst) == 4:
            if lst[1] == '+':

            elif lst[1] == '-':

            elif lst[1] == '*':
  
            elif lst[1] == '/':


        # 만약 정점이 단순한 숫자라면,
        else:
            tree[int(lst[0])] = int(lst[1])

