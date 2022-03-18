import sys
sys.stdin = open('input.txt')

plates = list(input())

ans = 0
for i in range(len(plates)):
    if i == 0:
        ans += 10
    elif plates[i] == plates[i-1]:
        ans += 5
    elif plates[i] != plates[i-1]:
        ans += 10
print(ans)