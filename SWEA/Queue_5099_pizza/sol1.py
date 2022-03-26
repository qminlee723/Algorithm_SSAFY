import sys

sys.stdin = open('input.txt')

def pizza(N, M, arr):
    # 화덕 준비
    Q = []

    # 화덕의 크기만큼 피자를 채워요 (N개만큼 채울 수 있음)
    # 방금 [0] 더해줬으므로 범위를 +1로 설정해줍니다.
    for i in range(N+1):
        Q.append(i) # 녹은 피자의 '번호'를 Q에다가 넣어줍니다.

    idx = N + 1 # 이 다음에 들어갈 피자 번호

    pizza_num = 0 # Q에서 데이터 접근하는 것 # while문 밖에 빼놓는 이유는 reset되지 않게 하려고

    while Q: # 화덕에 피자가 있는 동안에는 계속 돌아요(리스트에 원소가 있는 동안은 돌아요)
        # 화덕에서 입구에서 가장 근처에 있는 피자(즉, 가장 앞에 있는 피자)를 꺼낸다
        pizza_num = Q.pop(0) # 젤 앞에 있는거 꺼내준다 # top으로 꺼내줍니당

        # 1. 지금 꺼낸 피자에 치즈가 남았으면 //2
        if arr[pizza_num] // 2 != 0:
            # 치즈 녹이자
            arr[pizza_num] //= 2
            # 화덕의 맨 뒤에 넣어요
            Q.append(top)

        # 2. 피자를 넣어줘야 되는데 걍 무지성으로 넣으면 안됨
        elif idx <= M: # 남은 피자가 있어야 넣지
            # 화덕에 넣자
            Q.append(idx)
            # 다음 피자 준비
            idx += 1
    return pizza_num




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 피자 갯수와 index를 맞춰주기 위해서 앞에 [0]을 넣어줍니다.
    Ci = [0] + list(map(int, input().split()))

    # 피자 번호와 ci 값 넣을 queue 생성해주기
    pizza(N, M, arr)

    ans = 0
    print(f'{tc} {ans}')