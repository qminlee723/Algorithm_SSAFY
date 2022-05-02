import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 가로에 1~9가 다 오는지
    for i in range(9):
        for j in range(9):
            sudoku[i][j]
    # 세로에 1~9가 다 오는지
    for i in range(9):
        for j in range(9):




    # 3*3 칸에 1~9가 다 오는지
    square = 0
    for r in range(3):
        for c in range(3):
            square += sudoku[r][c]
