import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    sol=[]

    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                sol.append(arr[i][j])

    print(f'#{tc} {"".join(sol)}')