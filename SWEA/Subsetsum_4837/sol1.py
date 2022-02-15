import sys

sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 12개의 숫자를 원소로 가지는 집합 A 이므로 range를 13으로 줌
    A = [int(i) for i in range(1, 13)]

    cnt = 0
    for i in range(1<<len(A)):
        subset_lst = []                     # 빼내온 부분집합을 집어넣을 리스트
        summation = 0                       # 부분집합의 합을 구해야 하므로 변수
        for j in range(len(A)):
            if i & (1 << j):                # i의 부분집합일 때,
                subset_lst.append(A[j])     # 부분집합 리스트에 더해주고
                summation += A[j]           # 해당 부분집합을 더해주는 값을 도출
        if len(subset_lst) == N and summation == K:     #총 원소 수가 N이고, 원소의 합이 K인 숫자인 경우
            cnt += 1                                    # 카운트를 올려준다

    print(f'#{tc} {cnt}')



