def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    ai = list(map(int, input().split()))
    ai.sort(reverse=True)

    new_array = [0] * len(ai)
    if len(ai) % 2 == 0:
        middle = len(ai) // 2
        max_split = list_split(ai, middle)[0]
        min_split = list_split(ai, middle)[1]
        min_split.sort()

    for i in range(len(new_array)):
        if i % 2 == 0:
            new_array[i] = max_split[i//2]
        else:
            new_array[i] = min_split[i//2]
    print(new_array)



