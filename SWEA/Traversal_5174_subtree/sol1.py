import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    edge, node = map(int, input().split())
    arr = list(map(int, input().split()))

    vertex = edge + 1

    # 빈 배열을 만들어 줍니다
    c1 = [0] * (vertex + 1)
    c2 = [0] * (vertex + 1)

    # 배열 저장하기
    for i in range(edge):
        # 이진트리이므로 2를 곱해서 2개 쌍을 선택할 수 있게
        p, c = arr[i * 2], arr[i * 2 + 1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c


    # 전위 순회 + cnt
    cnt = 0
    def cnt_preorder(node):
        global cnt
        if node:
            cnt += 1
            cnt_preorder(c1[node])
            cnt_preorder(c2[node])
        return cnt

    cnt_preorder(node)
    print(f'#{tc} {cnt}')