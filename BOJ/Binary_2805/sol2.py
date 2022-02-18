import sys
sys.stdin = open('input.txt')

# 최댓값 구하는 함수
def my_max(lst):
    max_value = 0
    for i in lst:
        if max_value < i:
            max_value = i
    return max_value

n_tree, target = map(int, input().split())
tree_list = list(map(int, input().split()))

end = my_max(tree_list)
start = end - target

h = 0
while start <= end:
    h = (start+end)//2
    for i in tree_list:
        if i > h:
            h += (i-h)//2
        if h == target:
            print(h)
        if i < h:
            h += (i)
