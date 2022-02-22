import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    # 상 좌 우
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    move = 0

    # 출발점 찾기
    for c in range(len(ladder_list)):
        if ladder_list[99][c] == 2:
            break

    # 현재 위치 찾기
    r = 99

    while r > 0:
        new_r = r + dx[move]
        new_c = c + dy[move]

        if 0 <= new_r < 100 and 0 <= new_c < 100 and ladder_list[new_r][new_c] == 1:
            r = new_r
            c = new_c
            ladder_list[new_r][new_c] = 0
        move = (move + 1) % 3
    print(c)


#
#
# import sys
#
# sys.stdin = open('input.txt')
#
# for tc in range(10):
#     T = int(input())
#     ladder = [list(map(int, input().split())) fpr _ in range(100)]
#
#     # 출발점 찾기
#     if j in range(100):
#         if ladder[-1][j] == 2:
#             break
#
#     # i가 양수인 경우 올라갑니다.
#     i = 99
#     while i > 0:
#         i -= 1
#         # 왼쪽 확인
#         if j > 0 and ladder[i][j-1] == 1:
#             while ladder[i][j-1] == 1:
#                 j -= 1
#         # 오른쪽 확인
#         if j > 0 and ladder[i][j+1] == 1:
#             while ladder[i][j+1] == 1:
#                 j += 1
# #
# #
# #
# #
#
#
#
