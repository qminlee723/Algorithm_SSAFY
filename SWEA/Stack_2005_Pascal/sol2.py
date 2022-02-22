#창환이 풀이
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # arr = [[ 0 for _ in range(N) ] for _ in range(N) ]
    arr = []

    for i in range(N):
        sub_array = []
        for j in range(i+1):
            # 만약 위치가 arr의 양 끝이라면 1을
            if j == 0 or j == i:
                sub_array.append(1)
            else:
                sub_array.append(arr[i - 1][j - 1] + arr[i - 1][j])
        arr.append(sub_array)
    print(f'#{tc}')
    for a in arr:
        print(*a)