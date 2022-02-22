import sys


def is_sudoku(lst):
    for i in range(9):
        for j in range(1, 10):
            if j not in lst[i]:
                return False
    return True


def check_sudoku(lst):
    for r in range(0, 7, 3):
        for c in range(0, 7, 3):
            small_box = []
            for i in range(3):
                for j in range(3):
                    small_box.append(lst[r + i][c + j])
            if len(set(small_box)) != 9:
                return False
    return True


sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    if is_sudoku(puzzle) == True:
        transpose = list(zip(*puzzle))
        if is_sudoku(transpose) == True:
            if check_sudoku(puzzle) == True:
                print(f'#{tc} 1')
                continue

    print(f'#{tc} 0')



