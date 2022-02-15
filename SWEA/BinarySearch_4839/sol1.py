def bi_search(page, key): # binary search 정의
    start = 1           # 너무 당연하게 start = 0 으로 두고 , end page-1로 두고 풀었는데,
    end = page          # 아무리해도 안 나와서 문제 읽어보니 범위가 1~page
    cnt = 0
    while start <= end:
        cnt += 1        # while loop을 돌 떄마다 cnt 해서 작은 값을 가진 자가 우승자
        center = (start + end) // 2
        if center == key:
            return cnt
        elif center > key:
            end = center - 1
        else:
            start = center + 1
    return cnt

import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    page, pa, pb = list(map(int, input().split()))

    a = bi_search(page, pa)
    b = bi_search(page, pb)

    if a < b:   # 작은 값을 가진 자가 우승자
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')