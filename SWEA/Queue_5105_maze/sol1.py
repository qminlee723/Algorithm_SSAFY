
def visit():

    dx = [0, 0, -1, 1] # 상하좌우
    dy = [1, -1, 0, 0]


def bfs():
    visited = [0] * n
    queue = []
    queue.append(v)

    while queue:
        t = queue.pop(0)

        if not visited[t]:
            visited[t] = True
            visit(t)
        for i in lst(t):
            if not visited[i]:
                queue.append(i)

T = int(input())

for tc in range(1, T+1):

