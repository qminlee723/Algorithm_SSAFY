a = 1
b = 5

arr = ['T', 'B', 'T', 'S', 'A', 'K', 'L', 'I', 'Z', 'C']


arr2 = [0] * len(arr)
for i in range(len(arr)):
    if i < a or i >= a + b:
        arr2[i] = arr[i]
    else:
        if i == len(arr[a:b+a]) - 1:
            for j, value in enumerate(arr[a+3:b+a]):
                arr2[j+1] = value
        else:
            arr2[i+2] = arr[i]
print(*arr2)

#
#
# arr=['T','B','T','S','A','K','L','I','Z','C']
# index=list(map(int,input().split()))
#
# def LMove(st,ed):
#     temp=arr[st]
#     for i in range(st,ed,1):
#         arr[i]=arr[i+1]
#     arr[ed]=temp
#
# def RMove(st,ed):
#     temp=arr[ed]
#     for i in range(ed,st,-1):
#         arr[i]=arr[i-1]
#     arr[st]=temp
#
# for i in range (1):
#     LMove(index[0],index[1])
#
# print(*arr)