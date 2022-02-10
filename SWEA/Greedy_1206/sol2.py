import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    cnt = int(input())                    # 빌딩 수. 100개!
    buildings = list(map(int, input().split()))    # 빌딩 목록
    ans = 0                                     # 조망권이 확보된 세대

    for i in range(2, cnt-2):
        curr_height = buildings[i]

        if not curr_height:                     # 빌딩이 안 지어진 곳이라면
            continue

        else:
            max_height = 0                       # 이번 빌딩(i번째)을 기준으로, 양 옆 빌딩들 중 가장 높은 빌딩의 높이 저장

            # 양 옆 두 칸씩의 빌딩 높이를 구하기
            # 여기서 d = delta(변화량)
            d_col = [-2, -1, 1, 2]
            for d in d_col:
                # 현재 체크하는 빌딩의 인덱스에다 위 리스트의 값을 더해줌
                # 양 옆 두칸 빌딩의 인덱스
                check_idx = i + d

                if buildings[check_idx] > max_height:
                    max_height = buildings[check_idx]

            if curr_height > max_height:        # 조망권이 확보된 경우
                ans += curr_height - max_height



    print(f'#{tc} {ans}')

