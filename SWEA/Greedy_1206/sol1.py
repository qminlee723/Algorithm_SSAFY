import sys

sys.stdin = open('input.txt', 'r')
T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ## 조망권 확보된 세대 수 구하기
    cnt = 0
    for i in range(2, N-2): # 강변 양쪽 끝 2칸에는 건물이 존재하지 않는다
        # 각 건물별 조망권 계산
        # 인접한 네 건물 중 가장 큰 건물의 높이가 조망권 결정
        # maxV = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2]

        #slicing도 가능하지만, 시간이 초과될 수 있다
        # 새로운리스트 생성 > 탐색하면서 영역에 맞게 복사
        # for j in arr[i-2:i+3]

        maxV = 0 # arr[i-2]해도 괜찮음 # 인접 건물의 최대 높이를 저장히기 위한 변수
        for j in range(i-2, i+3):
            if i != j and maxV < arr[j]:
                    maxV = arr[j]

        result = arr[i] - maxV

        if result > 0:      # 조망권이 확보된 세대가 있으면
            cnt += result   # 총합에다 더하기

    print(f'#{tc} {cnt}')