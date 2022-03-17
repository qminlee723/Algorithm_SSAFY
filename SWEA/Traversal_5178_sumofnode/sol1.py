import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N: 노드 총 갯수 M: 리프노드 갯수 L: 출력할 노드 번호
    N, M, L = map(int, input().split())
    # 빈 배열 만들어 줌. 어짜피 leaf node이므로 하나만 만들어도 됨
    arr = [0] * (N + 1)

    for i in range(M):
        l_node, l_value = map(int, input().split())

    # 배열에 leaf값 저장
        for _ in range(M):
            arr[l_node] = l_value
        arr[L] = arr[L * 2] + arr[L * 2 + 1]
        if arr[L] =
