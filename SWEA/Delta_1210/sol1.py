# 먼저 사다리를 형성하는 값을 받아오고
# 가장 마지막 row에서 값을 2로 가지는 숫자의 인덱스를 찾는다
# 그곳을 출발점으로 삼아서 위로 올라간다.
# 위로 올라갈 때, 좌 우를 확인하면서 올라간다.
## 단, 좌
# 가장 상단에 (i < 0)서 더이상 갈 곳이 없는 경우 탐색을 중단하고, 그 곳의 값을 프린트한다.

import sys

sys.stdin = open('input.txt')

# 사다리표 받아오기
for _ in range(10):
    T = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]  # 비어있는 사다리

    # 출발점 찾기
    for j in range(len(ladder_list)):   # 어짜피 마지막 row를 체크할 것이기 때문에, 그 row에서의 element를 각각 확인
        if ladder_list[-1][j] == 2:     # 마지막 row에서 j 인덱스를 가지는 숫자가 2인 경우
            break                       # 그 곳이 출발점
    i = 99                              # 마지막 row 이므로 인덱스는 99일 것

    # 이제 출발점에서 움직여보자
    while i > 0:                                        # 가장 위로 올라와 더 이상 갈 곳이 없을 때 까지, 즉 i > 0 일 동안
        # 별 일 없으면 올라갑니다
        i -= 1                                          # i 에서 1씩 빼서 올라간다

        # 단, 양 옆을 확인해서 1이 있으면 그쪽으로 갑니다
        # 먼저 왼쪽 확인
        if j > 0 and ladder_list[i][j-1] == 1:          # 만약 j가 양수이고(즉, 표 안에 존재하고) j-1(왼쪽)가 가리키는 값이 1일 때
            while j > 0 and ladder_list[i][j-1] == 1:   # 그 값들이 계속 1을 가리키는 동안
                j -= 1                                  # j는 왼쪽으로 이동한다

        # 오른쪽 확인
        elif j < 99 and ladder_list[i][j+1] == 1:       # 만약 j가 99보다 작고(즉, 표 안에 존재하고) j+1(오른쪽)이 가리키는 값이 1일 때
            while j < 99 and ladder_list[i][j+1] ==1:   # 그 값들이 계속 1을 가리키는 동안
                j += 1                                  # j는 오른쪽으로 이동한다

    # 이제
    print(f'#{T} {j}')                                 # 이러한 과정을 끝마친 후, 인덱스 j를 반환한다
