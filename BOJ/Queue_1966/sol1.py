import sys
sys.stdin = open('input.txt')

lst = []
for i in range(9):
    num = int(input())
    lst.append(num)

max_num = max(lst)
print(max_num)

for j in range(9):
    if lst[j] == max_num:
        print(j+1)