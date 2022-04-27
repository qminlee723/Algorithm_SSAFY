import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    max_km, final_stop, stops_num = map(int, input().split())
    stops = list(map(int, input().split()))
    station = [0] * (final_stop + 1)
    cnt = 0
    now = max_km

    for stop in stops:
        station[stop] = 1

    whilecount = 0
    while now < final_stop:
        whilecount += 1
        if whilecount >= final_stop:
            print(f'#{tc} 0')
            break

        if station[now] == 1:
            cnt += 1
            now += max_km
        else:
            now -= 1
    if whilecount < final_stop:
        print(f'#{tc} {cnt}')