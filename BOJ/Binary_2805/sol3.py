import sys
sys.stdin = open('input.txt')

# 목표:  '적어도'  target만큼의 나무를 잘라내자!
n_tree, target = map(int, input().split())
height_tree = list(map(int, input().split()))
tallest = max(height_tree)

start = 0
end = max(height_tree)
result = 0
while start <= end: # 종료조건 설정
    len_tree = 0    # 돌 떄마다 초기화가 되어야 하니까 while loop안에
    middle = (start + end)//2
    for i in height_tree:   # for문을 돌면서, middle보다 높은 나무의 높이를 더해준다
        if i > middle:
            len_tree += i - middle
    if len_tree >= target:  # binary search
        result = middle
        start = middle + 1
    elif len_tree < target:
        end = middle - 1
print(result)