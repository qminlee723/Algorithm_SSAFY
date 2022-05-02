import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    sum_lst = list(map(int, input().split()))

    # M만큼 이웃하는 애들
    temp_sum = 0
    max_sum = 0
    min_sum = 987654321
    temp_lst = []
    for i in range(len(sum_lst)-M+1):
        for j in range(M):
            temp_sum += sum_lst[i+j]

        temp_lst.append(temp_sum)
        temp_sum = 0

    ans = max(temp_lst) - min(temp_lst)
    print(f'#{tc} {ans}')


    #     if temp_sum > max_sum:
    #         max_sum = temp_sum
    #     if temp_sum < min_sum:
    #         min_sum = temp_sum
    #     temp_sum = 0
    #
    # ans = max_sum-min_sum
    #
    # print(f'#{tc} {ans}')