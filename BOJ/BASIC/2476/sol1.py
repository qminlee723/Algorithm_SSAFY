import sys

sys.stdin = open('input.txt')

N = int(input())

gold_lst = []       # for 문 밖에 둬야함
for _ in range(N):
    a, b, c = map(int, input().split())


    if a == b == c:
        gold = 10000 + a * 1000
    elif a != b and b != c and a != c:
        max_num = max(a, b, c)
        gold = max_num * 100
    else:
        if a == b or a == c:
            gold = 1000 + a * 100
        elif b == c:
            gold = 1000 + b * 100

    gold_lst.append(gold)
max_gold = max(gold_lst)
print(max_gold)