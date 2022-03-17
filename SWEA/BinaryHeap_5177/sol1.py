import sys
sys.stdin = open('input.txt')

def enq(n): # 우선순위 큐
    global last
    last += 1
    tree[last] = n		# 완전이진트리 유지
    c = last			# 새로 추가된 정점을 자식으로
    p = c//2			# 완전이진트리에서의 부모 정점 번호

    while p >= 1 and tree[p] > tree[c]:			# 부모의 키 값이 자식보다 더 크면,
        tree[p], tree[c] = tree[c], tree[p]		# 부모와 자리 바꿔줌
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [0]*(N+1) # 인덱스 처리를 위해 1만큼 더 긴 리스트 생성
    last = 0

    # 트리 생성!
    for num in nums:
        enq(num)

    # 마지막노드의 조상 노드에 저장된 정수의 합을 알아내야 함
    # 조상 노드를 찾아준다
    ancestor = []
    while tree[N//2] != 0: # 조상 노드가 존재할 때
        ancestor.append(tree[N//2])
        N = N//2                # 찾은 부모를 새로운 자식으로 할당

    print(f'#{tc} {sum(ancestor)}')