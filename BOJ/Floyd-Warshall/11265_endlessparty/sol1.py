import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# Floyd-Warshall Algorithm
# 예제에서 초기 테이블을 이미 설정해줬으므로 그냥 쓰면 됨
# 이거 쓴 이후에는 해당 graph에 최단 거리 정보 가지게 됨
for k in range(n):
    for i in range(n):
        for j in range(n):
            # i 에서 j 가는 것 보다, i -> k -> j 가는 것이 더 적은 비용이 들 때 갱신
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m):
    a, b, c, = map(int, input().split())
		# 인덱스 에러 주의(1 <= a <= n, 1 <= b <= n)
		# a 는 출발점, b는 도착점, c는 비용
    if graph[a-1][b-1] <= c:
        print('Enjoy other party') #another
    else:
        print('Stay here')