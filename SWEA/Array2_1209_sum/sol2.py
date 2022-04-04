import sys

sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_value = 0
    max_row_sum = 0
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += arr[r][c]

        if max_row_sum < row_sum:
            max_row_sum = row_sum

    max_col_sum = 0
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += arr[r][c]

        if max_col_sum < col_sum:
            max_col_sum = col_sum

    dia1_sum = 0
    dia2_sum = 0
    max_dia_sum = 0
    for r in range(100):
        for c in range(100):
            if r == c:
                dia1_sum += arr[r][c]
                if max_dia_sum < dia1_sum:
                    max_dia_sum = dia1_sum
            if r + c == 99:
                dia2_sum += arr[r][c]
                if max_dia_sum < dia2_sum:
                    max_dia_sum = dia2_sum

    max_value = max(max_dia_sum, max_col_sum, max_row_sum)

    print(f'#{tc} {max_value}')
