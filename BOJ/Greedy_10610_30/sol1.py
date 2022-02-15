import sys

sys.stdin = open('input.txt')

# 숫자는 iterable하지 않으므로, string으로 받거나 list로 공백없는 정수를 받을 수 있다.
# 30 배수를 찾는게 나중에 계산이 필요할 거 같아서 그냥 정수로 받음
nums = list(input())
nums.sort(reverse=True)

number = int("".join(nums))

if number % 30 == 0:
    print(number)
else:
    print(-1)
# strings = [str(num)]
# strings = [str(integer) for integer in integers]
# a_string = "".join(strings)
# an_integer = int(a_string)
#
# #
# # # 30의 배수가 되려면 일단 받아온 리스트에 0이 존재해야 한다.
# #
# #
# # def bubble_sort(arr):
# #     for i in range(len(arr)):
# #         for j in range(len(arr)-i-1):
# #             if arr[j]>arr[j+1]:
# #                 temp = arr[j]
# #                 arr[j] = arr[j+1]
# #                 arr[j+1] = temp
# #     return arr
#
# def arrange(lst): # 카운팅 소트
#     cnt = [0] * (len(lst) + 1)
#     rlt = [0] * len(lst)
#
#     for idx in range(len(lst)):
#         cnt[lst[idx]] += 1
#
#     for cnt_idx in range(1, len(cnt)):
#         cnt[cnt_idx] += cnt[cnt_idx-1]
#
#     for i in range(len(lst)-1, -1, -1):
#         cnt[lst[i]] -= 1
#         rlt[cnt[lst[i]]] = lst[i]
#
#     return rlt
#
# # for num in nums:
# #     if nums[num] != 0:
# #         print('-1')
# #     else:
# #         multiply.append(nums[num])
# # # 뱉어낸 경우의 수가 30 배수인지 확인한다
# #
#
#
#
