import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    towers = int(input()) # x 축 길이!
    lst = list(map(int, input().split()))
    max_drop = 0

    for i in range(towers-1):
        now = lst[i]
        temp_drop = 0

        for j in range(i + 1, towers):
            if now > lst[j]:        # 기준이 되는 블럭이, 체크하는 블록보다 크다면 떨어질 공간이 있다는 것
                temp_drop += 1      # 떨어질 공간이 있다면 플러스 1 해주기
        if temp_drop > max_drop:
            max_drop = temp_drop


    print(f'#{tc} {max_drop}')

