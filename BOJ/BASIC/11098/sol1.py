import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    player_num = int(input())
    lst = []
    for i in range(player_num):
        cost, name = input().split()
        a = (int(cost), name)
        lst.append(a)
    lst.sort()
    print(lst[-1][1])
