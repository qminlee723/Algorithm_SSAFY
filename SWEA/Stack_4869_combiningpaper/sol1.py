import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    memo = [0, 1]

    for i in range(3, N // 10 + 1):
        memo.append(memo[i - 1] + memo[i - 2] * 2)
    # 이게 맞는지는 모르겠지만
    # 10 일 때 1, 20일 때 3 ... 식으로
    # 1 3 5 11 21 ... 이렇게 가는데
    # 1 + 3 + "1"
    # 3 + 5 + "3"
    # 5 + 11 + "5" ... 식으로 경우의 수가 가는 것 같아요?