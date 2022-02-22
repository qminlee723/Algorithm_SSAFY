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

    # 가장 일찍 오는 사람이 붕어빵 만드는 시간보다 일찍 온다면 실패!
    if my_min(arrival) < M:
        print(f'#{tc} Impossible')

    elif (M / K) * N > my_max(arrival):
        print(f'#{tc} Impossible')

    elif a
    # 모든 붕어빵을 만드는 시간이 가장 늦게 오는 시간보다 빠르면 성공!
    elif my_min(arrival) > M and N < K:
        if (M / K) * N <= my_max(arrival):
            print(f'#{tc} Possible')
    # 아니면 실패!
    else:
        print(f'#{tc} Possible')