import sys

# 1. 행 우선순회 하면서 각 행마다 합을 구하면 되고, 구한 합 중 최댓값만 저장
# 2. 열 우선순회 하면서 각 열마다 합을 구하면 됨, 구한 합 중 최댓값만 저장
# 3. 대각선은 ? 순회하면서 대각선에 포함되는 요소들 합을 구하고, 최대값이면 저장
# 4. 결과출력

##### 대각선 합을 어떻게 구하면 될지 생각 한번 해 보기

sys.stdin = open('input.txt', 'r')

#1. 100 * 100 matrix 초기화 하기
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for j in range(100)]

# 행의 합에서 최대값 구하기
    max_v = 0
    max_sum = 0 # 행, 열, 대각선 합 중 최댓값을 저장하는 변수
    # 각각의 요소의 합 구하기
    # 각가의 요소에 접근하기

    for r in range(len(arr)):
        row_sum = 0 # 각 행마다 합을 구해야 되기 때문에, 행의 시작점에서 변수 초기화
        for c in range(len(arr[0])):
            row_sum += arr[r][c]
        # 반복문이 끝나면 하나의 행을 순회
        if row_sum > max_sum:
            max_sum = row_sum

# 열의 값에서 최댓값 구하기
    for r in range(len(arr[0])):
        col_sum = 0
        for c in range(len(arr)):
            col_sum += arr[c][r]
            if col_sum > max_sum:
                max_sum = col_sum

    # 대각선의 값에서 최댓값 구하기
    # 모든 행을 다 수행을 해야지만 대각선에 해당하는 애들의 값의 합을 구할 수 있음
    dia1_sum = 0
    dia2_sum = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if r == c:
                dia1_sum += arr[r][c]
                if dia1_sum > max_sum:
                    max_sum = dia1_sum
            if r + c == len(arr[0])-1:
                dia2_sum += arr[r][c]
                if dia2_sum > max_sum:
                    max_sum = dia2_sum

    max_sum = max_sum if max_sum > dia1_sum else dia1_sum
    max_sum = max_sum if max_sum > dia2_sum else dia2_sum


    print(f'#{tc} {max_sum}')