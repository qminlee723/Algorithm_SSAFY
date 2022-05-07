import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 전략 모르겠고 다 가 본 다음에 몇개인지 세 보고 어느게 제일 짧은지 반환하자
    # 일단 시작점

    cnt_lst = []
    min_cnt = 987654321
    for j in range(100):
        if ladder[0][j] == 1:

            # 근데 여기선 시작점 여러개니까  포문 안에서 시작
            # i가 가장 바닥에 닿을 때까지(100) cnt를 셉니다
            i = 0
            cnt = 1
            y = j
            while 99 > i:
                i += 1
                cnt += 1

                # 왼쪽 확인
                if 0 < y and ladder[i][y-1] == 1:
                    while 0 < y and ladder[i][y-1] == 1:
                        y -= 1
                        cnt += 1

                # 오른쪽 확인
                elif 99 > y and ladder[i][y+1] == 1:
                    while 99 > y and ladder[i][y+1] == 1:
                        y += 1
                        cnt += 1

            if min_cnt >= cnt:
                min_cnt = cnt
                result = j

    print(f'#{T} {result}')

