import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(N):
    global cnt
    Q = deque()
    Q.append(N)
    visited = [0] * 1000001 # 조건이 1,000,000 까지 체크하는 것이므로

    while Q:
        w = Q.popleft()
        if visited[w]:
            continue

        visited[w] = 1

        if w == M:
            return cnt

        cnt += 1
        if 0 < w + 1 <= 1000000:
            Q.append(w+1)
        if 0 < w - 1 <= 1000000:
            Q.append(w-1)
        if 0 < w * 2 <= 1000000:
            Q.append(w*2)
        if 0 < w - 10 <= 1000000:
            Q.append(w-10)
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    ans = bfs(N)

    print(f'#{tc} {ans}')