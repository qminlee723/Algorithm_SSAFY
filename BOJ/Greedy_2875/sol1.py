import sys

sys.stdin = open("input.txt")

N, M, K = map(int, input().split())

## 1. 첫번째

# 일단 만족할 때 까지 돌립니다
team = 0
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


## 2.

# while N > 2 and M > 1 and N + M - 3 > K:
#     N -= 2
#     M -= 1
# team += 1
#
# print(team)