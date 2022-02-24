# ★ [백트래킹: 모든 경우의 수 탐색] 이거 그대로 외우자
# 트리구조 만들어지는 과정(피피티 부분집합 구하기 참고) -> 실행순서 손으로 꼭 써 보기
# 재귀함수를 통한 백트래킹
# a = [1, 2, 3]  -> 모든 부분 집합 나타내는 함수 써봐
# bit = [0] * N

def powerset(idx, N):
    # idx = index, N = total length
    if i == N:      # 종료 조건
        return

    else:
        bit[idx] = 0
        powerset(idx+1, N)

        bit[idx] = 1
        powerset(idx+1, N)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(a)
bit = [0] * N




def powerset2(idx, N):
    if idx == N:
        return


    # ## 아래부터 추가: 비트 자리에 있는 애 sum하고, 그게 3보다 크면 돌지마 #
    # check = 0
    # for i in bit:
    #     if bit[i]:
    #         check += a[i]
    #
    # if check > 3:
    #     return
    #
    # bit[idx] = 1
    # powerset(idx + 1, N)
    #
    # bit[idx] =
    # powerset(idx)
