import sys
import pprint
sys.stdin = open('input.txt')

my_bingo = [list(map(int, input().split())) for _ in range(5)]
ans_bingo = [list(map(int, input().split())) for _ in range(5)]

def calculate(my_bingo, ans_bingo):

# 내 빙고판을 돌면서, 사회자가 부르는 숫자를 찾으면 0으로 바꿔준다
    bingo = 0
    diag1 = False
    diag2 = False

    col = [False] * 5
    row = [False] * 5
    for i in range(5):
        for j in range(5):
            for r in range(5):
                for c in range(5):
                    if my_bingo[r][c] == ans_bingo[i][j]:
                        my_bingo[r][c] = 0

                        if not row[r] and sum(my_bingo[r]) == 0:
                            bingo += 1
                            row[r] = True
                        if not col[r] and sum(list(zip(*my_bingo))[r]) == 0:
                            bingo += 1
                            col[r] = True
                        if not diag1 and my_bingo[0][0] == 0 and my_bingo[1][1] == 0 and my_bingo[2][2] == 0 and my_bingo[3][3] == 0 and my_bingo[4][4] == 0:
                            bingo += 1
                            diag1 = True
                        if not diag2 and my_bingo[0][4] == 0 and my_bingo[1][3] == 0 and my_bingo[2][2] == 0 and my_bingo[3][1] == 0 and my_bingo[4][0] == 0:
                            bingo += 1
                            diag2 = True
                        if bingo >= 3:
                            return (i+1) * (j+1)

print(calculate(my_bingo, ans_bingo))