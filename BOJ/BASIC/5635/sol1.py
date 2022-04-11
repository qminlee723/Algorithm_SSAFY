import sys
sys.stdin = open('input.txt')

T = int(input())

lst = []
for tc in range(T):
    name, day, month, year = input().split()
    day, month, year = map(int, (day, month, year))
    lst.append((year, month, day, name))
lst.sort()

print(lst[-1][-1])
print(lst[0][-1])