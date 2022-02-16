
import sys

sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst_len = int(input())
    arr = list(map(int, input()))

    cnt = 0
    max_cnt = 0
    for i in range(lst_len):
        if arr[i] == 1:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0


    print(f'#{tc} {max_cnt}')