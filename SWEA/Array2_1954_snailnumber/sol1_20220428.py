import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # N * N 의 빈 배열을 만들어 주자
    arr = [[0] * N for _ in range(N)]

    #방향: 오른쪽->아래->왼쪽->위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    direction = 0

    # 시작점 (0.0)
    i = 0
    j = 0

    for n in range(1, N**2+1):
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
    print(f'#{tc}')
    for args in arr:
        print(*args)


