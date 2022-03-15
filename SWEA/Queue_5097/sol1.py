import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))


    for _ in range(M):
        t = queue.pop(0)        # queue에서 왼쪽을 pop해준다
        queue.append(t)         # 팝한 것을 다시 append해준다(제일 뒤로 감)
    print(f'#{tc} {queue[0]}')

    # deque 써서 popleft 가능할 듯
