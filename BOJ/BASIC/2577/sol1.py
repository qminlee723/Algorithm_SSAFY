import sys
sys.stdin = open('input.txt')

A = int(input())
B = int(input())
C = int(input())

num = A * B * C
str_num = list(str(num))

lst = []
for i in range(len(str_num)):
    lst.append(int(str_num[i]))

for j in range(10):
    print(lst.count(j))