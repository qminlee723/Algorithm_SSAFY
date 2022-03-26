import sys
from collections import defaultdict, deque

sys.stdin = open('input.txt')

def bfs(v):
    Q = deque()
    Q.append(v)

    visited[v] = 0

    while Q:
        w = Q.popleft()

        for value in default_dict[w]:
           if visited[value] == -1:
               Q.append(value)

               visited[value] = visited[w] + 1

    if visited[G] == -1:
        return 0
    return visited[G]



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [-1] * (V+1) # 동그라미 번호가 1부터 시작하거든요

    default_dict = defaultdict(list)
    for i in line:
        starting_node = i[0]
        end_node = i[1]
        default_dict[starting_node].append(end_node)
        default_dict[end_node].append(starting_node)
    print(default_dict)
    rlt = bfs(S)

    print(f'#{tc} {rlt}')

