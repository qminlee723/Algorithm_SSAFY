import sys
sys.stdin = open('input.txt')

# dfs(backtracking이니까 찍어봄)
def dfs(x, y, total):
    global result

    ##### 가지치기 (최솟값 갱신하기 전에 해서 계산 줄이기)
    if result < total:
        return
    # 종료조건
    if x == N-1 and y == N-1:
        # 토탈에다가 계속 더해주기
        total += arr[x][y]
        # 토탈 중 최솟값
        result = min(total, result)
        return result


    # arr탐색(2 방향 확인)
    for i in range(2):
        # 다음에 갈 곳들을 확인먼저하기
        ni = x + di[i]
        nj = y + dj[i]

        # 범위 설정해주기 (움직인 이후에도 arr안에 존재하도록)
        if 0 <= ni < N and 0 <= nj < N:
            # 방문한 적이 없다면
            if not visited[x][y]:
                # 방문했다고 1 표시 해주기
                visited[x][y] = 1
                # 그리고 현재 위치에 있는 숫자도 더해줘야함
                # 어떻게? 재귀로
                dfs(ni, nj, total+arr[x][y])
                # 종료 조건 만족해서 다시 처음으로 돌아갈 때 visit 표시 지워주기
                visited[x][y] = 0



# 방향 설정: 오른쪽, 아래
di = [0, 1]
dj = [1, 0]

# 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방문체크
    visited = [[0]*N for _ in range(N)]

    # 최솟값 찾는거니까 일단 비교하는 값으로는 최대값을 설정해주자
    result = 987654321

    # x, y, 그리고 최소합
    dfs(0, 0, 0)

    print(f'#{tc} {result}')