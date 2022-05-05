import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 가로 최댓값 구하기
    row_sum = []
    for i in range(100):
        row_sum.append(sum(arr[i]))
    max_row = max(row_sum)

    # 세로 최댓값 구하기
    col_sum = []
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += arr[j][i]
        col_sum.append(temp_sum)
    max_col = max(col_sum)

    # 우하향 대각선 합 구하기
    diag_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                diag_sum += arr[i][j]

    # 좌상향 대각선 합 구하기
    for i in range(99, 0, -1):
        rev_diag_sum = 0
        for j in range(100):
            rev_diag_sum += arr[i][j]

    the_max = [max_row, max_col, diag_sum, rev_diag_sum]
    print(f'#{tc} {max(the_max)}')