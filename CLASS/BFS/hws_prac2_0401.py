import sys
sys.stdin = open('input_hws')
from collections import deque


def bfs(v):
    queue = deque()  # 큐 생성
    # 시작 정점 1을 추가
    queue.append(1)
    visited[1] = 1

    while queue:
        v = queue.popleft()
        print(v)  # 삭제 후 출력
        for i in lst[v]:  # 정점의 값(인접한 정점) 탐색
            if visited[i] != 1:  # 방문한 적 없으면
                queue.append(i)  # 정점 추가
                visited[i] = 1  # 방문 처리


T = int(input())  # 테스트 케이스 수

for tc in range(T):
    N, M = map(int, input().split())  # 정점의 개수, 간선의 개수
    visited = [0] * (N + 1)  # 정점을 1부터 시작하려고 +1만큼 만듦
    lst = [[] for _ in range(N + 1)]  # 인덱스 : 정점, 값 : 인접한 정점 값

    for i in range(M):  # 인접한 두 정점 정보가 주어짐
        x, y = map(int, input().split())
        # 양방향으로 연결함
        lst[x].append(y)
        lst[y].append(x)

    bfs(1)  # bfs함수 호출