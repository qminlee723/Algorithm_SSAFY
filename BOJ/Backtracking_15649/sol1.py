import sys
sys.stdin = open('input.txt')

n, m = list(map(int, input().split()))
arr = []
def dfs():
    if len(arr) == m: # 조건
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if i not in arr: # i 가 쓰이지 않았을 때 # 가지치기
            arr.append(i)
            dfs()
            arr.pop()

dfs()