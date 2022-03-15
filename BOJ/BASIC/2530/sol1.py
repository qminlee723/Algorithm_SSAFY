import sys

sys.stdin = open('input.txt')

H, M, S = map(int, input().split())
duration = int(input())

if duration // 360 < 1:
    if duration // 60 == 0:
        M += duration // 60
        S += duration % 60
    else:
        M += duration // 60
        S += duration % 60
else:
    H += duration // 3600
    M += (duration - 3600*(duration // 3600)) // 60
    S += duration % 60

if M >= 60:
    H += M // 60
    M -= M // 60 * 60
elif S >= 60:
    M += S // 60
    S -= S // 60 * 60

print(H, M, S)
