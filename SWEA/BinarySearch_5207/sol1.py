import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 받아온 A는 정렬되어 있어야 한다
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    # B의 원소가 A 안에 존재하는지 확인
    for b in B:
        # start와 end를 지정해주고
        start = 0
        end = N - 1

        flag = 0
        # start가 end보다 작을 때, 즉 교차하기 전에
        while start <= end:
            # 중간점을 똑 뽀개서 찾아줍니다
            middle = (start + end) // 2

            # A의 가장 중간인 애보다 작을때랑 클 때가 있곘져
            # b가 A의 중간지점인 애보다 클 때
            if b >= A[middle]:
                # 같은거 찾으면 카운트 올려주고 그만
                if b == A[middle]:
                    cnt += 1
                    break

                start = middle + 1
                if flag == 1:
                    break
                flag = 1

            # b가 A의 중간지점인 애보다 작을 때
            elif b < A[middle]:
                end = middle - 1
                if flag == -1:
                    break
                flag = -1


    print(f'#{tc} {cnt}')