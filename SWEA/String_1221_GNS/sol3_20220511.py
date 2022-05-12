import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    tc, length = map(str, input().split())
    lst = list(input().split())

    # 작은 수부터 차례대로 정렬
    for i in range(int(length)):
        if lst[i] == 'ZRO':
            lst[i] = 0
        elif lst[i] == 'ONE':
            lst[i] = 1
        elif lst[i] == 'TWO':
            lst[i] = 2
        elif lst[i] == 'THR':
            lst[i] = 3
        elif lst[i] == 'FOR':
            lst[i] = 4
        elif lst[i] == 'FIV':
            lst[i] = 5
        elif lst[i] == 'SIX':
            lst[i] = 6
        elif lst[i] == 'SVN':
            lst[i] = 7
        elif lst[i] == 'EGT':
            lst[i] = 8
        elif lst[i] == 'NIN':
            lst[i] = 9

    ans_lst = sorted(lst)
    for i in range(int(length)):
        if ans_lst[i] == 0:
            ans_lst[i] = 'ZRO'
        elif ans_lst[i] == 1:
            ans_lst[i] = 'ONE'
        elif ans_lst[i] == 2:
            ans_lst[i] = 'TWO'
        elif ans_lst[i] == 3:
            ans_lst[i] = 'THR'
        elif ans_lst[i] == 4:
            ans_lst[i] = 'FOR'
        elif ans_lst[i] == 5:
            ans_lst[i] = 'FIV'
        elif ans_lst[i] == 6:
            ans_lst[i] = 'SIX'
        elif ans_lst[i] == 7:
            ans_lst[i] = 'SVN'
        elif ans_lst[i] == 8:
            ans_lst[i] = 'EGT'
        elif ans_lst[i] == 9:
            ans_lst[i] = 'NIN'

    print(tc)
    print(' '.join(ans_lst))
