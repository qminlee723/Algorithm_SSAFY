import sys; sys.stdin = open('input.txt')

pwd = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

#======================================
N, M = map(int, input().split())

lines = set() # set이 중복을 제거한다는 것에 착안해서
for _ in range(N):
    arr = input()
    lines.add(arr)
# print(lines)

for i in lines:
    print(i)

