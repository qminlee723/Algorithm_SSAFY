import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))


i = 0
j = 0
cnt = 0
while i < len(arr):
    if arr[i] > M:
        i += 1
        continue
    elif arr[i] == M:
        cnt += 1
        i += 1
        continue
    j = i + 1
    add = arr[i]
    while j < len(arr):
        add += arr[j]
        if add == M:
            cnt += 1
            break
        elif add > M:
            break
        j += 1
    i += 1
print(cnt)