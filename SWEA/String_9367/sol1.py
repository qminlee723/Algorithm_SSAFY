import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    # (어짜피 자기 자신을 포함한 것도 길이니까 1로 두자)
    cnt = 1
    max_value = 1

    for i in range(1, arr_len):
        if arr[i-1] < arr[i]:
            cnt += 1
            if max_value < cnt:
                max_value = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_value}')