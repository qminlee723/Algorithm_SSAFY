n = 2
arr = [3, '#', 1, '#', 2, '#', 8, '#', 9]

nums = arr[::2]
arr2 = [0] * len(nums)
j = 0
for i, v in enumerate(nums):
    if i >= len(nums) - n:
        arr2[j] = v
        j += 1
        # for j, value in enumerate(nums[len(nums)-n:len(nums)]):
        #     arr2[j] = value
        # break
    else:
        arr2[i+n] = v

final_arr = ['#'] * len(arr)
for i, v in enumerate(arr2):
    final_arr[i * 2] = v
print(final_arr)
