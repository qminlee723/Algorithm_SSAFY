# import sys
#
# sys.stdin = open('input.txt')

# N = int(input())
# lights = list(map(int, input().split()))
# s_num = int(input())
#
#
# for _ in range(s_num):
#     gender, num = map(int, input().split())
#
#     # 만약 성별이 남자라면, 3을 받았으면 3이랑 6번째 전구를 바꿔야함
#     if gender == 1:
#         for i in range(1, len(lights)):
#             if i % num == 0:
#                 if lights[i-1] == 1:
#                     lights[i-1] = 0
#                 elif lights[i-1] == 0:
#                     lights[i-1] = 1
#
#     # 만약 성별이 여자라면, 3을 받았으면 3번 전구를 바꾸고, (2, 4)번 전구를 바꾸고, (1, 5)번 전구를 바꿔야 함
#     if gender == 2:
#         if lights[num - 1] == 1:
#             lights[num - 1] = 0
#         elif lights[num - 1] == 0:
#             lights[num - 1] = 1
#         for j in range(1, N//2):
#             # IndexError 나지 않게 범위 설정
#             if num-1-j < 0 or num-1+j > N:
#                 break
#             if lights[num - 1 - j] == lights[num - 1 + j]:
#                 if lights[num - 1 - j] == 0:
#                     lights[num - 1 - j] = 1
#                     lights[num - 1 + j] = 1
#                 else:
#                     lights[num - 1 - j] = 0
#                     lights[num - 1 + j] = 0
#             else:
#                 break
#
#         for k in range(1, N+1):
#             print(lights[k-1], end=' ')
#             if k % 20 == 0:
#                 print('')


import sys

sys.stdin = open('input.txt')

N = int(input())
lights = [-1] + list(map(int, input().split()))
s_num = int(input())


for _ in range(s_num):
    gender, num = map(int, input().split())

    # 만약 성별이 남자라면, 3을 받았으면 3이랑 6번째 전구를 바꿔야함
    if gender == 1:
        for i in range(len(lights)):
            if i % num == 0:
                if lights[i] == 1:
                    lights[i] = 0
                elif lights[i] == 0:
                    lights[i] = 1

    # 만약 성별이 여자라면, 3을 받았으면 3번 전구를 바꾸고, (2, 4)번 전구를 바꾸고, (1, 5)번 전구를 바꿔야 함
    if gender == 2:
        for j in range(N//2):
            # IndexError 나지 않게 범위 설정
            if num-j < 0 or num+j > N:
                break
            if lights[num - j] == lights[num + j]:
                if lights[num - j] == 0:
                    lights[num - j] = 1
                    lights[num + j] = 1
                else:
                    lights[num - j] = 0
                    lights[num + j] = 0
            else:
                break

for k in range(1, N+1):
    print(lights[k], end=' ')
    if k % 20 == 0:
        print('')