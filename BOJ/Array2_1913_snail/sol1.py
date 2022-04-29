import sys
sys.stdin = open('input.txt')

# N = int(input())
# target = int(input())
# arr = [[0]*N for _ in range(N)]
#
# # 방향: 상 > 우 > 하 > 좌
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
# direction = 0
#
# # 시작점
# i = N // 2 + 1
# j = N // 2 + 1
#
# for n in range(1, N**2+1):
#     arr[i][j] = n
#     i += di[direction]
#     j += dj[direction]
#
#     if


# 뭔가 반복되는 코드가 엄청 많아서 좀 줄이려고 발악해봤지만
# 로직을 더이상 못찾겠어서 계속 코드 반복 했습니다
# 인덱스 에러 그만 보고싶어요

N = int(input())
target = int(input())

# N * N 의 빈 배열을 만들어 주자
arr = [[0] * N for _ in range(N)]

# 방향: 하>우>상>좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
direction = 0

# 시작점 (0.0)
i = 0
j = 0

for n in range(N**2, 0, -1):
    arr[i][j] = n
    i += di[direction]
    j += dj[direction]

    # i, j 가 배열 밖을 벗어나거나,
    # arr[i][j]가 0이 아닐 경우, 즉, 이미 지나간 길일 경우
    if i < 0 or i >= N or j < 0 or j >= N or arr[i][j]:
        i -= di[direction]
        j -= dj[direction]

        # 방향은 4가지니까 3까지 다 돌면 다시 reset해줘야 함
        # 이것도 for k in range(4) 해서 하려고 했는데 돌릴 위치를 못찾았다
        if direction >= 3:
            direction = 0
            i += di[direction]
            j += dj[direction]
        else:
            direction += 1
            i += di[direction]
            j += dj[direction]

for arg in arr:
    print(*arg)
for i in range(N):
    for j in range(N):
        if arr[i][j] == target:
            print(i+1, j+1)
