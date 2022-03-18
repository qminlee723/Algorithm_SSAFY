import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    exam = list(input())

    score = 0
    total_score = 0
    for i in exam:
        if i == 'O':
            score += 1
            total_score += score
        elif i == 'X':
            score = 0
    print(total_score)
