arr = ['A', 'T', 'B', 'T', 'S']

n = 2
arr2 = [0] * len(arr)
for i in range(len(arr)):
    if len(arr) - n <= len(arr):
        if i == len(arr) - n:
            for j, value in enumerate(arr[len(arr) - n:]):
                arr2[j] = value
            break
        else:
            arr2[i + n] = arr[i]
    else:
        a = -n
        arr2[i-a] = arr[i]
print(arr2)
