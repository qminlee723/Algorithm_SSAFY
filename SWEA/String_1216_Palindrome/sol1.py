import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    board = list(input() for _ in range(100))

    board_c = list(zip(*board))

    # 무조건 정사각형(100*100)
    # A 도 길이 1짜리 회문
    # 가로 확인해서 가장 긴 회문 길이
    # 세로 확인해서 가장 긴 회문 "길이"

    max_len = 0
    for i in range(100):
        for j in range(101):
            if board[i][j:-j] == board[i][j:-j][::-1]:
                if max_len < len(board[i][j:-j]):
                    max_len = len(board[i][j:-j])


    for i in range(100):
        for j in range(101):
            if board_c[i][j:-j] == board_c[i][j:-j][::-1]:
                if max_len < len(board_c[i][j:-j]):
                    max_len = len(board_c[i][j:-j])

    print(f'#{tc} {max_len}')