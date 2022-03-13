import sys

sys.stdin = open('input.txt')

H, M, S = map(int, input().split())
duration = int(input())

if duration // 3600 < 1:
    if duration // 60 < 1:
        S += duration
    else:
        M += duration // 60
        S += (duration - (duration // 60) * 60) % 60
else:
    H += duration // 3600
    M += (duration - 3600 * (duration // 3600)) // 60
    S += duration % 60

# 작은 단위부터
if S >= 60:
    M += S // 60
    S -= S // 60 * 60

if M >= 60:
    H += M // 60
    M -= M // 60 * 60

if H >= 24:
    H = 0

print(H, M, S)

H = H + (duration + M * 60 + S) // 3600
M =
print(H)