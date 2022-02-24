import sys

sys.stdin = open('input.txt')

test = 10
for tc in range(1, test + 1):
    n = int(input())
    arr = [list(map(int, input().split()) for _ in range(n))]
    answer = 0

    for j in range(n):                      # 한 열씩 확인
        temp = []
        for i in range(n):                  # 밑으로 내려가면서 빨 파 확인
            if arr[i][j] == 1:              # 좌표에 빨간 것이 있으면
                temp.append(1)
            if arr[i][j] == 2 and temp:     # temp 배열에 어떤 값이 있다면
                answer += 1
                temp = []

    print('#{} {}'.format(tc, answer))