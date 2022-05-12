import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr_col = list(zip(*arr))
    # 가로확인
    max_len = 1
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(101 - max_len):
                if arr[i][j] == arr[i][j:j+k][::-1]:
                    max_len += 1

    max_len_col = 1
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(101 - max_len_col):
                if arr_col[i][j] == arr_col[i][j:j+k][::-1]:
                    max_len_col += 1


    if max_len > max_len_col:
        print(f'#{T} {max_len}')
    else:
        print(f'#{T} {max_len_col}')


