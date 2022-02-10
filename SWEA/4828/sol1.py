import sys

sys.stdin = open('input.txt')

T = int(input())            # test case 갯수
# n개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오

for tc in range(1, T + 1):
    N = int(input())        # 양수의 갯수
    ai = list(map(int, input().split()))    # N개의 양수

# 가장 큰 수 찾기
    # 최댓값에 0 을 집어넣고 input 숫자들과 비교
# 가장 작은 수 찾기
    # 최솟값에 주어진 숫자보다 큰 수 집어넣고 input 숫자들과 비교

    max_v = 0
    min_v = 1000001

    for i in ai:
        if i > max_v:  #만약 i가 max_v보다 크다면
            max_v = i  # max_v에 i 의 값을 집어넣어준다 => 최댓값 찾기!

        if i < min_v:
            min_v = i   # 똑같이 최솟값 찾기!

        ans = max_v - min_v # 최댓값 - 최솟값
    print(f'#{tc} {ans}')




