# import sys
#
# sys.stdin = open('input.txt')
#
# # input은 이제 주석 생략
# T = int(input())
#
# for tc in range(1, T + 1):
#     int_cnt, sec_cnt = map(int, input().split())  # int_cnt = N, sec_cnt = M
#     integers = list(map(int, input().split())) # integers = ai
#
#     max_value = min_value = integers[0]
#     for i in range(int_cnt - sec_cnt + 1):
#         result = 0
#         for j in range(i, i + sec_cnt):
#             result += integers[j]
#         if result >= max_value:
#             max_value = result
#         if result <= min_value:
#             min_value = result
#     ans = max_value - min_value
#
#
#     # for i in range(len(integers) - sec_cnt + 1):
#     #     summation = sum(integers[i: i+sec_cnt])
#     #     if summation > max_value:
#     #         max_value = summation
#     #     if summation <= min_value:
#     #         min_value = summation
#     #
#     # ans = max_value - min_value
#     print(f'#{tc} {ans}')
#
#
# N, M, K = map(int, input().split())

    # 일단 만족할 때 까지 돌립니다
    while True:
        # 팀을 구성할 때 N 두 명, M 1명이 필요하니 전체 숫자에서 그 숫자들을 빼 줍니다
        N -= 2
        M -= 1

        # 그 숫자들을 뺀 값들이 다음 팀을 결성하기 위해 충분하기 위해서는
        # 남아있는 N이 2보다 커야하고, M이 1보다 커야하고, N+M이 K보다 커야합니다
        # 이를 조건문으로 적어주면

        if N < 0 or M < 0 or N + M < K:
            break
        team += 1

    print(team)
