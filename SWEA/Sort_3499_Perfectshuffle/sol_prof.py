import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    words = input().split()

    mid_index = n // 2
    ans = []

    index = 1

    if n % 2 == 0:
        for i in range(n):
            if i < mid_index:
                ans.append(words[i])
            else:
                ans.insert(index, words[i])
                index += 2

    else:
        for i in range(n):
            if i < mid_index+1:
                ans.append(words[i])
            else:
                ans.insert(index, words[i])
                index += 2

    print('#{}'.format(tc), *ans)
