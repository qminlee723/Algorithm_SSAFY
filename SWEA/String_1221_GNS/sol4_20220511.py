import sys
sys.stdin = open('input.txt')

GNS_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2,
            'THR': 3, 'FOR': 4, 'FIV': 5,
            'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for _ in range(1, T+1):
    tc, length = map(str, input().split())
    lst = list(input().split())

    value_lst = []
    for i in lst:
        value_lst.append(GNS_dict[i])

    value_lst.sort()

    print()
    print(tc)
    for v in value_lst:
        for key, value in GNS_dict.items():
            if v == value:
                print(key, end=" ")