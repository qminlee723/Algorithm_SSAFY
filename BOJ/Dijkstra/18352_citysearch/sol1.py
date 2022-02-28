import sys
import heapq
sys.stdin = open('input.txt')
INF = int(1e9)

# N = 도시의 갯수, M = 도로의 갯수, K = 타겟 거리, X = 출발 도시 번호
N, M, K, X = map(int, input().split())

#A와 B에 대한 정보 담는 빈 리스트 생성
graph = [[] for _ in range(N + 1)]

# 최단 거리 테이블 생성 (첨에는 전부 무한대로 초기화 -> 최단 경로로 갱신)
distance = [INF] * (N + 1)


# A = 출발 도시, B = 도착 도시
for _ in range(M):
    A, B = map(int, input().split())
    # 문제에서는 비용이 없으므로 일단 0으로 둔다 ( X )
    # 가중치 1
    graph[A].append((B, 1))


# Dijkstra
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X)

ans = []
for i in range(1, N + 1):
    if distance[i] == K:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i, end='\n')


# 최단 거리가 K 인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
# 단, 해당 조건을 만족하는 도시가 없으면 -1을 출력
