import sys
sys.stdin = open('input.txt')

C = int(input())
for tc in range(C):
    classmates = list(map(int, input().split()))
    class_avg = (sum(classmates)-classmates[0]) // classmates[0]

    cnt = 0
    for i in classmates[1:]:
        if i > class_avg:
            cnt += 1
    ans = cnt  / classmates[0] * 100
    print("%.3f%%" %ans)
