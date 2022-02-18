# 교수님 풀이
import sys
sys.stdin = open('input.txt')

def count_arr(N):
    ret = 0
    for i in range(N+1):
        cnt = 0 # 열을 쭉 돌아야 하니까
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))

    ### DRY RULE ### => 하지만 일단 이걸 만들어 놓고 함수를 만들자! (오류 피하기)
    # # row
    # sol = 0
    # for i in range(N+1):
    #     cnt = 0 # 열을 쭉 돌아야 하니까
    #     for j in range(N+1):
    #         if arr[i][j] == 1:
    #             cnt += 1
    #         else:
    #             if cnt == K:
    #                 sol += 1
    #
    #
    # # column
    # sol = 0
    # for i in range(N+1):
    #     cnt = 0 # 열을 쭉 돌아야 하니까
    #     for j in range(N+1):
    #         if arr[j][i] == 1:
    #             cnt += 1
    #         else:
    #             if cnt == K:
    #                 sol += 1


    sol = count_arr(N)
    arr = list(map(list, zip(*arr)))
    sol += count_arr(N)

    print(f'#{tc} {sol}')




    # 2차원 배열에서 range를 정확하게 두고
    