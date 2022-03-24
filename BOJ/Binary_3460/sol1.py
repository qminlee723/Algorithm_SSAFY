import sys
sys.stdin = open('input.txt')


T = int(input())

def FindBinary(N, lst):
    a, b = divmod(N, 2)
    if a == 0 and len(lst) < 3:
        lst.append(0)
        return FindBinary(N, lst)
    elif a == 0 and len(lst) >= 4:
        lst.append(b)
        return lst
    elif a != 0:
        lst.append(b)
        return FindBinary(a, lst)


N = int(input())

lst = []
b_num = FindBinary(N, lst)
sorted(b_num, reverse=True)
print(b_num)

for i in range(len(b_num)):
    if b_num[i] == 1:
        print(i, end=' ')

