import sys

# 최댓값 구하는 함수
def my_max(lst):
    max_value = 0
    for i in lst:
        if max_value < i:
            max_value = i
    return max_value

sys.stdin = open('input.txt')

# 목적: len_tree를 제공할 수 있는 최종 H를 구해야 함
# 적당한 H의 시작점: 젤 높은 나무 - 원하는 나무길이

# 나무 수 #원하는 나무길이
n_tree, len_tree = map(int, input().split())
height_tree = list(map(int, input().split()))

tallest = my_max(height_tree)
end_h = 0
start_h = tallest - len_tree

while start_h
while start_h != end_h:
    middle = (start_h + end_h) // 2
    if height_tree[middle] == len_tree:
        print(len_tree)
        break
    elif height_tree[middle] > len_tree:
        end_h= middle - 1
    else:
        start_h = middle + 1



# for i in range(n_tree):
#     if height_tree[i] > h:
#         timber += height_tree[i] - h
#         if timber > len_tree:
#             h += (tallest - h)//2
#         elif timber == len_tree:
#             print(h)
#         elif timber < len_tree:
#             h - ()
#
#
# start = tallest - len_tree
# end = tallest
# while start <= tallest:
#     middle = (start+end)//2
#     if height_tree[middle]

