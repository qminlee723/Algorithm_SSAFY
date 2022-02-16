import sys

sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    # 출발점 찾기
    for j in range(len(ladder_list)):
        if ladder_list[-1][j] == 2:
            break
    i = 99

    # 움직이는 로직
    while i > 0:
        if j > 0 and ladder_list[i][j-1]