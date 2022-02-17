import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(input())

    board_c = list(zip(*board))

    for i in range(n):
        for j in range(n-m+1):
            if board[i][j:j+m] == board[i][j:j+m][::-1]:
                print(f'#{tc} {board[i][j:j+m]}')

    for i in range(n):
        for j in range(n-m+1):
            if board_c[i][j:j+m] == board_c[i][j:j+m][::-1]:
                rlt = ''.join(board_c[i][j:j+m])
                print(f'#{tc} {rlt}')