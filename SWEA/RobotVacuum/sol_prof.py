import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split()) # arr 배열 크기
y, x, d = map(int, input().split()) # 좌표 방향 0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 로봇 청소기의 뒤를 보기 위한 좌표
ny = [1, 0, -1, 0]
nx = [0, -1, 0, 1]

ans = 1             # 청소기 놓자마자 일단 한 곳 청소
arr[y][x] = 3       # 청소 한 곳은 X이라고 체크
check = 0           # 방향 체크 # "왼쪽으로" 돌면서 체크

while 1:
    if d == 0:      # 왼쪽으로 돌기 때문에 북쪽 다음엔 서쪽을 봐야됨
        d = 3      # 보고 나면 청소
    else:
        d -= 1
    if arr[y+dy[d]][x+dx[d]] == 0:  # 왼쪽을 봤는데 청소가 안 되어 있다면,
        y += dy[d]                  # 이동 후 기준 좌표 값 바꿔주고
        x += dx[d]
        arr[y][x] = 3               # 청소하기
        ans += 1                   # 청소 횟수 올려주기
        check = 0                     # 방향 체크는 0으로 바꾸기
    else:
        check += 1

    if check == 4:
        if arr[y + ny[d]][x + nx[d]] == 1:     # 뒤가 벽이라면
            break
        elif arr[y + ny[d]][x + nx[d]] == 0:   # 뒤가 비어 있다면
            y += ny[d]                      # 기준 좌표값 바꿔주고(이동
            x += nx[d]
            arr[y][x] = 3                   # 청소하기
            ans += 1                        # 청소 횟수 올려주기
            check = 0
        else:                               # 이미 뒤가 비어있지 않고 청소한 곳이라면
            y += ny[d]
            x += nx[d]
            check = 0

print(ans)