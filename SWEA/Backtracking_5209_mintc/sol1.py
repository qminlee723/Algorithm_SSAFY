import sys
sys.stdin = open('input.txt')

def dfs(v, cnt):
    global result

    # 종료조건
    if v == N:
        if result > cnt:
            result = cnt
        return

    if result < cnt:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(v+1, cnt + V[v][i])
            visited[i] = 0
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 98765321

    print(f'#{tc} {dfs(0, 0)}')