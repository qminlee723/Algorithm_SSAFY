import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    N = int(input())

    dic = {}
    max_value = 0
    for _ in range(N):
        uni, liter = input().split()
        dic[uni] = int(liter)
        if dic[uni] > max_value:
            max_value = dic[uni]

    # dict.items(): key value의 쌍을 튜플로 묶은 값을 객체로 돌려준다.
    for key, value in dic.items():
        if value == max_value:
            print(key)
