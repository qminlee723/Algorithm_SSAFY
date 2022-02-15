# import sys
#
# sys.stdin = open('input.txt')
#
# T = int(input())
# n_list = list(map(int, input().split()))
# n = len(n_list)
#
# for i in range(1 << n):# 원소 10개, 2^10개가 부분집합 갯수
#     subsets = []
#     for j in range(n):                  # 각 부분집합에 10개씩 비트를 읽어주고
#         if i & (1 << j):    # i의 j번째 비트 - 즉 부분집합을 빼 와서 리스트에 넣는다.
#             subsets.append(n)
#     total = 0
#     for subset in subsets:      # 리스트 안의 부분집합을
#         total += subset         # 더해서
#         if total == 0:          # 합이 0일 경우
#             print(1)            # 1을 프린트
#         else:
#             print(0)            #아니면 0을 프린트
#

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    cnt = 0
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(numbers[j])
        if len(subset) != 0 and sum(subset) == 0:
            cnt += 1

    if cnt > 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')