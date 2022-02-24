def partition(arr, start, end):
    #pivot
    pivot = arr[(start + end) // 2]

    while start <= end:

        # start
        while arr[start] < pivot:
            start += 1

        # end
        while arr[end] > pivot:
            end -= 1

        # 엇갈리지 않았다면,
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start] #swap
            start += 1
            end -= 1
    return start

def quicksort(arr, start, end):
    part2_idx = partition(arr, start, end)
    if start < end:
        quicksort(arr, start, part2_idx - 1)
        quicksort(arr, part2_idx, end)


lst = [5, 7, 1, 2, 3, 2, 2, 6, 67, 2, 54, 5]
quicksort(arr=lst, start=0, end=len(lst)-1)
print(lst)




## PYTHONIC 한 버전

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot, other = arr[0], arr[1:]
#     left = [x for x in other if x <= pivot]
#     right = [x for x in other if x > pivot]
#     return quicksort(left) + [pivot] + quicksort(right)
#
#
# lst = [69, 10, 30, 2, 16, 8, 31, 22]
# print(lst)
#
# sorted_lst = quicksort(arr=lst)
# print(sorted_lst)