def func(lst):
    # 가로 검사
    for i in range(9):
        total = 0
        for j in range(9):
            total += lst[i][j]
        if total != 45:
            return 0
    return 1

    # 세로 검사

def func
    for i in range(9):
        total = 0
        for j in range(9):
            total += lst[j][i]
        if total != 45:
            return 0

    # 네모 검사
    for i in (0, 3, 6):
        for j in 0, 3, 6


t = int(input())
for tc in range(1, t+1):
