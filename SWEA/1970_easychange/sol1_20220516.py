import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans_list = []
    for i in range(len(money_list)):
        change = N // money_list[i]
        ans_list.insert(i, change)
        if change > 0:
            N -= change * money_list[i]

    print(f'#{tc}')
    for ans in ans_list:
        print(ans, end=' ')
    print()