arr = [3, 4, 1, 1, 2]

arr2 = [0] * len(arr)
for i in range(len(arr)):
    if i == len(arr) - 1:
        arr2[0] = arr[i]
    else:
        arr2[i + 1] = arr[i]
print(arr2)