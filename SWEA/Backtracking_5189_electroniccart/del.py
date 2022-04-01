import sys
sys.stdin = open('input.txt')

# s = start, cnt = 몇 번 갔는지, acc = 지나간 곳 누적값
def dfs(s, cnt, acc):
    global result

    # 종료조건
    if acc >= result:
        return

    # 갈 수 있을때까지 갔다면
    if cnt == N-1:
        # 다시 1번 사무실로 돌아와야함
        acc += arr[s][0]
        # result와 acc 중 더 작은걸 result에 넣어주자 (최솟값 구하는 것)
        result = min(result, acc)


    else:
        # 이제 column 위치 찾아주자
        for w in range(1, N):
            # 아직 방문하지 않았다면
            if not visited[w]:
                # visited 상태를 1로 바꾸어주고
                visited[w] = 1
                # dfs를 돌려서 탐색해주자
                dfs(w, cnt + 1, acc + arr[s][w])
                # 해당 경우의 수를 다 탐색헀으면, 그 부분을 0으로 다시 갱신해줌
                visited[w] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 987654321

    dfs(0, 0, 0)
    print(f'#{tc} {result}')