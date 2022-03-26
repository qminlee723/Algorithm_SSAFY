import sys

sys.stdin = open('input.txt')

def bfs(v):
    Q = []
    Q.append(v)

    # 방문 했어요 표시
    visited[v] = 1

    while Q:
        # 제일 앞에 있는 친구 나오세요
        w = Q.pop(0)

        for i in range(V+1):
            # 만약 field에 w에서 출발해서 i로 가는 애가 있으면면
           if field[w][i] == 1 and visited[i] == 0:
               Q.append(i) # 연결된 다음 번호 큐에 넣기

               # 이전 방문 정보에 +1 == 이동한 거리
               visited[i] = visited[w] + 1

    if visited[G]: # Goal이라면
        return visited[G] - 1
    else: # 도착하지 않았다면. visited가 0일 때! -> -1 해주면 [-1]이 되니깐 따로 else로 빼준 것
        return visited[G]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [0] * (V+1) # 동그라미 번호가 1부터 시작하거든요

    # 인접 행렬 만들기
    # 0으로 초기화된 인접 행렬을 만들어줍니다.
    field = [[0 for _ in range(V+1)] for _ in range(V+1)]

    ### 아래의 이거나 바로 위의 한줄이나 똑같음
    # matrix = []
    # for i in range(V+1):
    #     row = [0]*(V+1)
    #     matrix.append(row)


    # 연결된 곳 1로 만들기
    for each in line:

        start = each[0]
        end = each[1]

        field[start][end] = 1
        field[end][start] = 1
    print(field)
    rlt = bfs(S)

    print(f'#{tc} {rlt}')

