
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Data = list(map(int, input().split()))
    cnt = 0
    Data = merge_sort(Data)