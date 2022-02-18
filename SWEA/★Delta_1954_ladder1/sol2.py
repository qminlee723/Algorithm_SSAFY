import sys
sys.stdin = open('input.txt')

for _ in range(10):
    n = int(input())

    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))

    # 상, 좌, 우 순
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    move = 0

    x = 99
    # 마지막 줄에서 도착지점이 있는 곳 찾기(2 찾기)

    for i in range(100):
        if board[99][i] == 2:
            y = i
            break


