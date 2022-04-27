import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for j in range(N):
        if j >= 2:
            if arr[j-1] < arr[j] and arr[j-2] < arr[j] and arr[j+1] < arr[j] and arr[j+2] < arr[j]:
                building = max(arr[j-1], arr[j-2], arr[j+1], arr[j+2])
                cnt += arr[j] - building
    print(f'#{tc} {cnt}')