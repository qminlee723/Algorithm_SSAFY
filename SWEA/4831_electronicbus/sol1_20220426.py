import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    max_km, final_stop, stops_num = map(int, input().split())
    stops = list(map(int, input().split()))

    cnt = 0
    for j in range(3):
        if j > 1 and stops[j] - stops[j-2] <= max_km:
            if stops[1] - stops[0] < max_km:
                cnt = 1
            else:
                cnt = 0
        elif 0 <= j <= 1 and stops[1]-stops[0] == max_km:
            cnt = 2

    for i in range(stops_num):
        if i > 0 and stops[i] - stops[i-1] > max_km:
            cnt = 0
            break
        elif i > 1 and stops[i] - stops[i - 2] >= max_km:
            cnt += 1

    if final_stop - stops[-1] > max_km:
        cnt = 0

    print(f'#{tc} {cnt}')
