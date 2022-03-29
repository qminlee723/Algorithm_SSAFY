import sys
sys.stdin = open('input.txt')

# dfs 함수 구현(출발점)
# 1. 종료조건
# 2. 함수호출
# 3. 가지치기

# cnt = 내가 몇번 움직였나?
def dfs(coords, cnt, total):
    # 가장 작은 배터리 소모량이 저장되어 있는 글로벌 변수 지정
    global result



    # 1. 종료조건: 모든 방을 다 돌고, 처음 방으로 돌아올 것
    # 즉, visited의 모든 값이 1일 때
    # 방문한 모든 방들의 값들을 더해준다
    if 0 not in visited:
        total += arr[x][y]
    # 종료하기 전에, 돌면서 더했던 값들의 합이 현재 가지고 있는 값보다 작으면 최솟값으로 갱신해주기
        if total < min_count:
            min_count = total
            return min_count

    # 함수호출 파트
    # tc1의 경우: (0,0) => (0,1) => (1,2) => (2,0)
    #                  => (0,2) => (2,1) => (1,0) 으로 두가지 경우의 수 나옴
    # (0, y) => (y, x) => (x, 0) 의 순서....라고 생각..해도..되냐 .....
    for i in range(N):
        arr[i]




    # 지금 내가 가지고 있는 가중치, 현재 가장 작은 가중치 비교

# 가지치기
# 만약 내가 가지고 있는 가중치 > 현재 가장 작은 가중치 이면
# 바로 리턴해주자


# else


 # 뭔가 조작(A)을 하고
            # visited(2) = 1 해놔~~

        # 재귀 호출을 해요
        # 조작한 A를 다시 돌려요


# 인풋
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    elements = [list(map(int, input().split())) for _ in range(N)]
    # visited list 생성 (1차원만 있으면 됨 - 방문했는지 1, 0만 확인해주면 되니까)
    # result, min_count (결과 저장할 변수)
    visited = [0] * N
    total = 0
    min_count = 987654321
    # dfs, bfs, search( ) 등 함수 구현해줍시다
    dfs(0, 0, 0)

    print(f'#{tc} ')