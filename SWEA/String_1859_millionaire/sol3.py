# 단일루프로 풀고싶을 때
# 거꾸로 가보자 (오 -> 왼)

# 교수님 풀이2 (룹이 한 번 도니까 더 빠르게 가능!)
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    sol = 0
    mmax = lst[N-1]
    for i in range(N-2, -1, -1):
        if mmax < lst[i]:
            mmax = lst[i]
        else:
            sol += (mmax - lst[i])

    print(f'#{tc} {sol}')
