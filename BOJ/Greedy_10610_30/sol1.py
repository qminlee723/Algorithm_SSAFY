import sys

sys.stdin = open('input.txt')

# 숫자는 iterable하지 않으므로, string으로 받거나 list로 공백없는 정수를 받을 수 있다.
# 30 배수를 찾는게 나중에 계산이 필요할 거 같아서 그냥 정수로 받음
nums = list(map(int, list(input())))

# 30의 배수가 되려면 일단 받아온 리스트에 0이 존재해야 한다.

def cnt_sort(lst):
    empty_list_for_num_count = [0] * (len(lst))
    

for num in nums:
    if nums[num] != 0:
        print('-1')
    else:
        multiply.append(nums[num])
# 뱉어낸 경우의 수가 30 배수인지 확인한다




