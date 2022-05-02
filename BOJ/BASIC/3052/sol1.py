import sys
sys.stdin = open('input.txt')
lst = []
for i in range(10):
    num = int(input())
    lst.append(num)

my_set = set()
for j in lst:
    remainder = j % 42
    my_set.add(remainder)
print(len(my_set))









