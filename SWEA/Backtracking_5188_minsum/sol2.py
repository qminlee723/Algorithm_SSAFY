import sys

sys.stdin = open('input.txt')

# dfs
def dfs(s, cnt, acc):
    global result

    # 만약 다 더해진게 현재 가진 값보다 크다면, 볼 필요 없음
    if acc >= result:
        return

    # 만약 2번(=N-1)을 갔다면, 볼것도 없이 더 못가니까 그 자리에 있는 숫자 acc에 더해주고
    # acc와 result 비교해서 작은거 반환
    if cnt == N - 1:
        acc += arr[s][0]
        result = min(result, acc)

    else:
        for w in range(N):
            # s == w 이면 해당 좌표의 값이 0이므로, 그렇지 않은 것들의 값을 소환해야하니깐 조건을 줍니당
            # 그리고 방문되지 않은 곳만!
            if s != w and not visited[w]:
                # 방문 갱신해주고
                visited[w] = 1
                # 새로운 dfs의 세계로 들어가봅니다
                dfs(w, cnt + 1, acc + arr[s][w])
                # 그 dfs의 세계가 끝나면(return)되면
                # 이어서 가줍니다. 일단 이 부분은 가본 거니까 안가본데 가야됨!방문 갱신
                visited[w] = 0

    return


# 인풋
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 최솟값 구해야되니까 줄 수 있는 최댓값을 줍니당
    result = 987654321

    dfs(0, 0, 0)
    print(f'#{tc} {result}')