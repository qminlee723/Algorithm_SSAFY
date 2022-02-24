import sys

def my_sum(lst):
    summation = 0
    for i in lst:
        summation += i
    return summation

def my_max(lst):
    max_value = 0
    for i in lst:
        if max_value < i:
            max_value = i
    return max_value

def my_min(lst):
    min_value = 987654321
    for i in lst:
        if min_value > i:
            min_value = i
    return min_value


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrival = list(map(int, input().split()))

    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[arrival[i]] += 1

        for j in range(1, len(cnt)):
            cnt[i] += cnt[i-1]

        rlt = [0] * N
        for k in range(N):
            index = arrival[i]
            rlt[cnt[index]-1] = arrival[i]
            cnt[index] -= 1




# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arrival = list(map(int, input().split()))
#
#     # 가장 일찍 오는 사람이 붕어빵 만드는 시간보다 일찍 온다면 실패!
#     if my_min(arrival) < M:
#         print(f'#{tc} Impossible')
#
#     # 붕어빵 만드는 총 시간이 가장 늦게 오는 사람보다 늦어지면 실패!
#     elif (M / K) * N > my_max(arrival):
#         print(f'#{tc} Impossible')
#
#
#     else:
#         print(f'#{tc} Possible')