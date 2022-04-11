# # 1. 리스트에 55 44 33 22 11 0 for문 이용하여 차례로 집어넣기
# lst = []
# for i in range(55, -1, -11):
#     lst.append(i)
# print(lst)
#
# # 2. lst안에 있는 알파벳 중 중복을 제거하고 알파벳 순서대로 넣기
# lst = ['A', 'B', 'T', 'A', 'A', 'A', 'B', 'A']
# print(sorted(list(set(lst))))
#
# # 3. 재귀호출
# lst = [10, 9, 8, 7, 6, 6, 7, 8, 9, 10]
# def call(v):
#     if v == 5:
#         return
#     print(v)
#     call(v-1)
#     print(v)
# call(10)
#
# def BFS(v):
#     Q = []
#     Q.append(v)
#
#     while Q:
#         w = Q.pop(0)
#
#         for r in range(4):
#             ni = w[0] + di[r]
#             nj = w[1] + dj[r]
#
#             arr[ni][nj] += 1
#     return arr
#
#
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
# arr = [[0] * 4 for _ in range(4)]
# v = arr(1, 1)
# BFS(v)
