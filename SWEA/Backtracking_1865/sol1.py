import sys
sys.stdin = open('input.txt')

# w = worker number, per = 확률값
def dfs(w, per):
    global result

    # 가지치기
    # visited를 체크하기 때문에 하나씩 빼지만 15만 돌아가도
    # 아주아주 많이 커진다
    # 그래서 가지치기를 해줘야됨
    # 어느 경우를 제외해 줄 수 있을지 고민해봅시다.
    # 현재 내가 가지고 있는 확률이 , 어떤 확류를 곱하면 작아질지?
    # 지금 최대 확률을 구하는거니까, 지금 내가 몇 번째의 일꾼인지는 고나계 없음
    # global 에 저장된느 result보다 작으면 어짜피 곱할때니까 더 작아짐
    # global에 있는 result보다 작으면, 더 이상 이 밑을 확인할 필요가 없다.
    if per <= result:
        return

    # 만약에 같은 경우는?
    # if per == result:
    #     # a) w 가 전체 일꾼이 선택이 되었을 때 -> 할 필요 없음
    #     # b) w가 전체 일꾼이 선택되지 않았을 때 -> 할 필요 없음
    #     return


    # 종료조건
    if w == N:
        result = max(result, per)
        return

    # 아직 모든 일꾼이 선택되지 않았을 때
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1  # 조작하고
                dfs(w+1, arr[w][i]*per) # dfs
                visited[i] = 0  # 이 다음에 dfs 할 준비



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 이거 각각의 숫자를 확률로 변환해서 풀어야 한다
    # arr안의 숫자에다 100을 나눠서 확률로

    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100

    visited = [0] * N
    result = 0

    # 1을 넣는 이유는
    dfs(0, 1)
    # 확률은 곱할수록 값이 작아지므로 가지치기가 가능하다

    # 출력 형식이 다른거 확인하고 바꿔준다
    # 퍼센테이지로 다시 바꿔주고 7번째 줄에서 반올림
    print(f'#{tc} {result*100:6f}')
