import sys

sys.stdin = open('input.txt')

def func(n, m, k, lst): # n = len(lst)
    bucket = [0] * 11112
    #  손님을 버켓에 등록
    for item in lst:
        bucket[item] -= 1

    # 누적합 구하면서 m초에 해당하는 인덱스에 도달하면..
    # 버켓을 값을 k 개 증가
    # 버켓의 값을 확인헀을 때, 음수이면 꺼버리기

    if bucket[0] < 0:               # 만약 손님이 0초에도 온다면,
        return 'Impossible'

    for i in range(1, len(bucket)): # 0 초 이후에 손님들 도착 -> 손님 1초 부터 옴
        bucket[i] += bucket[i-1]    # 누적합 구하기
        if (i % m) == 0:            # 빵이 나온다면(m의 배수에 해당하는 인덱스)
            bucket[i] += k
        if bucket[i] < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    lst = map(int, input().split())
    result = func(n, m, k, lst)
    print(f'#{tc} {result}')