import sys

sys.stdin=open('input.txt')

# 종현님 풀이

T = 10
def ladder(c):
    r = 99                              # r의 초기 값은 99
    # 델타
    # 좌 우 상
    dr=[0,0,-1]
    dc=[-1,1,0]
    direction = 0                       # 방향 0
    while True:
        if r <= 0:                      # r이 0 보다 작거나 같으면 break
            break
        new_r = r + dr[direction]       # direction 방향 탐색
        new_c = c + dc[direction]
        # new_r 과 new_c 인덱스 체크
        if 0<= new_r < 100 and 0<= new_c < 100:     # new_r 과 new_c 가 범위 안에 있는 경우
            if ladders[new_r][new_c] == 1:          # direction 방향에 1이 있을 때
                r = new_r                           # r 값 변경
                c = new_c                           # c 값 변경
                ladders[new_r][new_c] = 0           # 갔던 길은 0으로 초기화
        direction = (direction + 1) % 3             # direction 은 0, 1, 2 만 나와야함 ( 달팽이 )
    return c

def find_2(arr):
    for i in range(len(arr)):
        if arr[99][i] == 2:
            y = i
    return y

for tc in range(1, T + 1):
    N = int(input())
    ladders = [list(map(int,input().split())) for _ in range(100)]
    rlt = ladder(find_2(ladders))
    print(f'#{tc} {rlt}')




#한지희

import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    a = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                y = j  # 도착 지점 찾기
    visit = [[0] * 100 for _ in range(100)]
    x = 99  # 맨 밑에서부터 시작
    while x > 0:  # 0번째 줄(첫째 행)까지
        visit[x][y] = 1
        if y - 1 >= 0 and arr[x][y - 1] and visit[x][y - 1] == 0:  # 왼쪽으로 가기
            y -= 1
            continue
        elif y + 1 < 100 and arr[x][y + 1] and visit[x][y + 1] == 0:  # 오른쪽으로 가기
            y += 1
            continue
        x -= 1  # 한 줄 위로 올라가기
    print(f'#{a} {y}')


# 경하님 풀이
for _ in range(10):
    n = int(input())
    #도착점이 2이므로 도착점으로부터 역으로 이동
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    #위(0), 왼쪽(1), 오른쪽(2)
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    move = 0

    x = 99
    #마지막 줄에서 도착지점이 있는 위치 찾기
    for i in range(100):
        if board[99][i] == 2:
            y = i
            break

    while True:
        #위로 이동 중일 때
        if move == 0:
            #범위 내이고 왼쪽에 막대기가 있으면 방향을 왼쪽으로 전환
            if y-1 >= 0 and board[x][y-1] == 1:
                move = 1
            #범위 내이고 오른쪽에 막대기가 있으면 방향을 오른쪽으로 전환
            elif y+1 <= 99 and board[x][y+1] == 1:
                move = 2
        #왼쪽으로 이동 중 세로 방향의 막대기를 만나면 위로 방향 전환
        elif move == 1:
            if board[x-1][y] == 1:
                move = 0
        #오른쪽으로 이동 중 세로 방향의 막대기를 만나면 위로 방향 전환
        else:
            if board[x-1][y] == 1:
                move = 0

        x += dx[move]
        y += dy[move]
        #첫줄에 도달하면 종료
        if x == 0:
            break
    #종료시점에서 위치를 출력
    print(f'#{n} {y}')



# 승윤님 풀이
import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]  # 데이터 받기

    for i in range(100):
        if num_list[0][i] == 1:  # 첫줄이 1로 시작하면 시작 포인트로 잡고 내려가기 시작
            x, y = 0, i  # 포인트값
            direction = 'down'  # 시작 방향은 무조건 아래이므로 down으로 시작
            while True:
                # 우측 끝에 없고 우측에 1이 있으며 그 전 진행 방향이 아래 혹은 오른쪽 일때,
                if y < 99 and num_list[x][y + 1] == 1 and (direction == 'down' or direction == 'right'):
                    y += 1
                    direction = 'right'

                # 좌측 끝에 없고 좌측에 1이 있으며 그 전 진행 방향이 아래 혹은 왼쪽 일때,
                elif y > 0 and num_list[x][y - 1] == 1 and (direction == 'down' or direction == 'left'):
                    y -= 1
                    direction = 'left'

                # 사다리 끝에 도달했는데 그 값이 2일때 (당첨일 때)
                elif x == 99 and num_list[x][y] == 2:
                    print(f'#{tc} {i}')
                    break

                # 사다리 끝에 도달했지만 2가 아닐 때,
                elif x == 99:
                    break

                # 이외의 경우는 아래로 한칸 내려감
                else:
                    x += 1
                    direction = 'down'

        else:
            pass