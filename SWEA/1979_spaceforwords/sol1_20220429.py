import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 일단 커다란 빈 배열을 만들어서
    # 하나하나 넣어줘야겠다
    arr = [[2] * (N+2) for _ in range(N+2)]
    for k in range(1, N+1):
        arr[k] = [2] + list(map(int, input().split())) + [2]

    # 가로줄 확인

    # 4개 짜리 이상은 카운트 하면 안되는데, 자꾸 3개까지 reach 하면 row_cnt 가 올라가서 해결하기 빡셈
    # 그리고 마지막 111 같은 경우, else에 안걸려서 자꾸 row_cnt 를 올리지 않고 바로 지나가버림
    ## 그래서 받아와주는 테두리를 0, 1이 아닌 다른 숫자로 덮으면 좋겠다고 생각했음
    row_cnt = 0
    for i in range(N+2):
        cnt = 0
        for j in range(N+2):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    row_cnt += 1
                cnt = 0

    # 세로줄 확인
    col_cnt = 0
    for i in range(N+2):
        cnt = 0
        for j in range(N+2):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    col_cnt += 1
                cnt = 0

    print(f'#{tc} {row_cnt + col_cnt}')