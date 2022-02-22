# import sys
#
# sys.stdin = open('input.txt')
#
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# print(board)
#
#     visit = [[0] * N for _ in range(N)]
#
#     queue = [[0, 0]]
#
#     #아래, 오른쪽
#     dx = [1, 0]
#     dy = [0, 1]
#
#     #BFS
#
#     while queue:
#         x, y = queue[0][0], queue[0][1]
#         del queue[0]
#         jump = board[x][y]
#
#         if jump == -1:
#             print("HaruHaru")
#
#         for i in range(2):
#             new_x = x + dx[i] * jump
#             new_y = y + dy[i] * jump
#
#             if 0 <= new_x < N and 0 <= new_y < N and visit[new_x][new_y] == 0:
#                 visit[new_x][new_y] = 1
#                 queue.append([new_x, new_y])
#     print("Hing")
#
import sys
sys.stdin = open('input.txt')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = set()
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    value = board[x][y]

    if value == -1:
        print("HaruHaru")
        exit(0)

    if [x,y] not in visited:
        visited.add([x,y])

        # 하, 우
        dfs(x + value, y)
        dfs(x, y + value)

# 시작점
dfs(0,0)
print("Hing")
