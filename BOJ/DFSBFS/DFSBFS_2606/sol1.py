import sys

#
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end='')
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

sys.stdin = open('input.txt')

N = int(input())
couple = int(input())


def dfs(r, c):
    for i in range():
        rr, cc = r + dr[i], c + dc[i]
        if 0 <= rr < N and 0 <= cc < M:
            visited[rr][cc] = True
            dfs(rr, cc)



def dfs()