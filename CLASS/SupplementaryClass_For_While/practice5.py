n = 3
arr = [3, '#', 1, '#', 2, '#', 8, '#', 9]

arr2 = [0] * len(arr)
for i in range(len(arr)):
    if arr[i] == '#':
        arr2[i] = arr[i]
    elif i == 0:
        arr2[n*2] = arr[i]
    else:
        for j, value in range()


print(arr2)