
import sys

sys.stdin = open('input.txt')


# #창환이 풀이

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     # arr = [[ 0 for _ in range(N) ] for _ in range(N) ]
#     arr = []
#
#     for i in range(N):
#         sub_array = []
#         for j in range(i+1):
#             # 만약 위치가 arr의 양 끝이라면 1을
#             if j == 0 or j == i:
#                 sub_array.append(1)
#             else:
#                 sub_array.append(arr[i - 1][j - 1] + arr[i - 1][j])
#         arr.append(sub_array)
#     print(f'#{tc}')
#     for a in arr:
#         print(*a)


# 교수님 풀이

T = int(input())

memo = [[0] for _ in range(11) for _ in range(11)]

for i in range(11):
    for j in range(i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]


for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(f'{memo[i][j]}', end = "")
        print()
