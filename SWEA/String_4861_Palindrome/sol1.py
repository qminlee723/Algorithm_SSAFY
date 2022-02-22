import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    for i in range(N):
        a = board[i]
        if a == a[::-1]:
            print(a)


    for r in range(M):
        board_c = []
        for c in range(N):
            board_c.append(board[c][r])

        for i in range(N-M+1):
            if board_c[i:i+M] == board_c[i][i+M][::-1]:
                print("".join(board_c))
































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