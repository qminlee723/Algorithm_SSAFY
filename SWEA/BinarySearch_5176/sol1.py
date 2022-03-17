import sys
sys.stdin = open('input.txt')


def inorder(node):      # 중위순회로 찾아줍니다
    global cnt          # 재귀함수 내에서 계속 호출하기 번거로우므로(사실 어떻게 하는지 모르므로) global 써줍니다
    if node <= N:       # 노드 수만큼 돌자
        inorder(node*2)     # 왼쪽
        tree[node] = cnt    # 자식이 없으면 카운트 숫자 저장
        cnt += 1            # 카운트 하나 올려주기
        inorder(node*2+1)   # 오른쪽

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)      # 빈 배열을 만들어줍니당

    cnt = 1                 # 카운트는 1부터 들어가니까
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')  # 루트값, N//2 번 노드 값 출력
