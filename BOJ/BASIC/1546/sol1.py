import sys
sys.stdin = open('input.txt')

N = int(input())
scores = list(map(int, input().split()))
high_score = max(scores)

temp_score = 0
for score in scores:
    temp_score += score / high_score * 100

fake_avg = temp_score / N
print(fake_avg)