n = 2
arr = [9, 3, 5, 7, 4] # 74935

# print(arr[len(arr)-n:] + arr[:n+1])

arr2 = [0] * len(arr)
for i in range(len(arr)):
    if i == len(arr) - n:
        for j, value in enumerate(arr[len(arr)-n:]):
            arr2[j] = value
        break
    else:
        arr2[i+n] = arr[i]

print(arr2)

