import sys
from collections import defaultdict

sys.stdin = open('input.txt')

def bfs(v):
    Q = []
    Q.append(v)

    # 방문 했어요 표시
    visited[v] = 0

    while Q:
        # 제일 앞에 있는 친구 나오세요
        w = Q.pop(0)

        # 그냥 딕셔너리 일때는 키가 딕셔너리에 있는지 확인
        # 딕셔너리에 그 키가 없으면, 얘는 리프 노드라는 뜻 - 마지막
        # if w not in normal_dict:
        #     continue
        for value in default_dict[w]:
            # 만약 field에 w에서 출발해서 i로 가는 애가 있으면면
           if visited[value] == -1:
               Q.append(value) # 연결된 다음 번호 큐에 넣기

               # 이전 방문 정보에 +1 == 이동한 거리
               visited[value] = visited[w] + 1

    if visited[G] == -1: # 한 번이라도 visit을 안 했으면,
        return 0
    return visited[G]



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [-1] * (V+1) # 동그라미 번호가 1부터 시작하거든요

    # 인접 행렬 만들기
    # 0으로 초기화된 인접 행렬을 만들어줍니다.
    default_dict = defaultdict(list)
    normal_dict = {}
    for i in line:
        starting_node = i[0]
        end_node = i[1]
        default_dict[starting_node].append(end_node)
        #
        if starting_node not in normal_dict:
            # 엔드노드는 엠티 리스트에다가 넣은거다 # 헷갈리면 창환이가 또 때림
            normal_dict[starting_node] = [end_node]
        else:
            normal_dict[starting_node].append(end_node)






    ### 아래의 이거나 바로 위의 한줄이나 똑같음
    # matrix = []
    # for i in range(V+1):
    #     row = [0]*(V+1)
    #     matrix.append(row)

    rlt = bfs(S)

    print(f'#{tc} {rlt}')

