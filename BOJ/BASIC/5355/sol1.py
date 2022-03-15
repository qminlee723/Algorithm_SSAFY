import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    mars = list(map(str, input().split()))
    ans = 0
    for i in range(len(mars)):
        if i == 0:
            ans += float(mars[i])
        else:
            if mars[i] == "@":
                ans *= 3
            elif mars[i] == "%":
                ans += 5
            elif mars[i] == "#":
                ans -= 7
    print("%0.2f" % ans)