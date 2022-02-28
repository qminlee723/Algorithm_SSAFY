import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, p = map(int, input().split())
    base = [list(map(int, input().split())) for _ in range(n)]

    # 최대 몇 마리의 바이러스 퇴치가 가능한가?
    virus = 0

    # 게임판의 크기 설정(n*n)
    for i in range(n):
        for j in range(n):

            # 가로와 대각선의 기준점을 정한다
            row, cro = base[i][j], base[i][j]

            # 폭탄 범위 정하기
            # 폭탄이 power만큼 양 옆으로 퍼져나간다
            for k in range(-p, p + 1):

                # k가  0 이 아니면,
                if k != 0:

                    # 세로 방향으로 터질 때, 0보다 크고 n 보다 작은 범위에서 터질 것
                    if 0 <= i + k < n:

                        # 세로 방향으로 터지면서 잡은 바이러스 갯수 더함
                        row += base[i + k][j]

                        #  대각선 확인
                        if 0 <= j + k < n:

                            # 대각선 방향으로 터지면서 잡은 바이러스 갯수 더함
                            cro += base[i + k][j + k]

                        # 왼쪽 대각선, 0 보다 크고 n보다 작은 범위에서 터짐
                        if 0 <= j - k < n:

                            # 왼쪽 대각선 방향으로 터지면서 잡은 바이러스 갯수 더함
                            cro += base[i + k][j - k]

                    # 가로 방향으로 터질 때 범위 안에서 터질 것
                    if 0 <= j + k < n:

                        # 가로 방향으로 터질 때 잡은 바이러수 갯수 더함
                        row += base[i][j + k]

            # 바이러스가 없거나, 바이러스가 최대값보다 작을 때,
            if not virus or virus < max(row, cro):

                # 최댓값을 바이러스에 할당해준다
                virus = max(row, cro)
    print(f'#{tc} {virus}')




