import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs(start):
    Q = deque()
    # Queue에다가 시작점을 넣어줍니당
    Q.append(start)

    # 방문 체크 해준다
    # 첫 스타트 지점의 거리는 1이야
    visited[start[0]][start[1]] = 1

    # Q 안에 뭐든 들어있으면 돌립시다
    while Q:
        # 제일 처음 들어온 자료를 빼내주고
        w = Q.popleft()

        # 4방향을 봐 줘야될것같죠?
        for i in range(4):
            # 4 방향을 확인해서 0이 있으면 진행하고, 1이 있으면 그만둬야겠져?
            # 다음 ij를 찾아봅시다
            ni = w[0] + di[i]
            nj = w[1] + dj[i]
            # 만약 다음 ij, 즉 ni, nj가 0 이면 가고, 1 이면 안가요
            # 그런데 0 이면 가고 나서 visited 체크를 해줘야해요
            # 그리고 범위를 벗어나면 안되겠죠? 그리고 인덱스는 0으로 시작한다는거 잊지 말기!
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] == 1:
                    continue
                # 생각해보니 0이면  가긴 가는데, 대신 안 가본 0이어야됨
                elif maze[ni][nj] == 0 and visited[ni][nj] == 0:
                    # 새로운 시작점이 돼야되니까 일단 Queue에다가 집어넣고
                    # 튜플 집어넣는거니까 ni, nj 이렇게 넣지말고 (ni, nj)로 넣어줍시당
                    Q.append((ni, nj))
                    # visited체크도 해주죠
                    visited[ni][nj] = 1
                    # 근데 visited에 들어가는건 뭐다?
                    # 시작점과의 "거리"다
                    # 그러면 거리를 체크해줘야되니까 가는 길마다 1은 더해줘야지
                    visited[ni][nj] = visited[w[0]][w[1]]+1

                # 응 이제 종료해야되겠져?
                # 3을 만나면 끝나니까 그걸 조건문 처리해줍시다
                elif maze[ni][nj] == 3:
                    #############근데 왜 여기서 빼기 1을 해줘야되는거지?
                    return visited[w[0]][w[1]] -1
                # 오 근데 생각해보니까 못만나는 경우는 0 처리를 해 줘야된다그럤음
                # 0은 언제 나와야 되는게 맞을까 생각해보면
                # Queue가 비었을 때 일걸
                # 그니까 while문 바깥에 써주자
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N) ]

    # 일단 시작점 지정해줘야함
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    # 시작점에서 방향체크해서 갈 수 있는 곳 확인
    # 상하좌우
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    # visited가 정의가 안됐다고 에러가 났네?
    # 정의해주자
    visited = [[0] * N for _ in range(N)]

    print(bfs(start))

    # 오 출력이 000002가 나왔어
    # 어제의 실수를 생각해보면 return 0 의 위치가 잘못된거 같애

    # 오 출력이 77072가 나왔어
    # 뭔가 잘못됐네
    # 그래도 0은 고쳐진거 같으니까 7을 다시보러가자
