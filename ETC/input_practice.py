# ## 정수 하나 받기
# n = int(input())
#
# a, b = map(int, input().split())
#
# ## 띄어쓰기가 있는 정수 입력받아서 list에 넣기
# lst1 = list(map(int, input().split()))
# lst2 = [map(int, input().split())]
#
# ## 띄어쓰기가 없는 정수 입력받아서 리스트 만들기
# # input 1234
# lst3 = list(input())
# # print: ['1', '2', '3', '4']
# lst3 = list(map(int, list(input())))
# # print: [1, 2, 3, 4]
#
#
# ## 2차원 리스트
# # input
# # 1 2 3 4
# # 5 6 7 8
#
# # 먼저 빈 리스트를 만들어 두고
# matrix = []
# # 2 번 받을 거니까
# for _ in range(2):
#     row = list(map(int, input().split()))
#     # print(row) == [1, 2, 3, 4]
#     matrix.append(row)
#     #print(matrix) == [[1, 2, 3, 4], [5. 6. 7. 8]]
#
#
# # 위랑 똑같은 결과 도출 가능
# # _ 로 쓴다는 것은 이걸 이용하지 않겠다는 것 - listmapintinput 이 코드를 2번 반복하겠다는 것
#
# matrix_2 = [ x for x in range(10)]
# matrix = [list(map(int, input().split())) for _ in range(2)]





## Shallow Copy
# lst 자체에 lst를 할당하는 순간, 얕은 복사
lst = [1, 2, 3, 4]
temp = []
temp.append(lst)

lst.pop()
lst.insert(0, 5)

print(temp)
# print: [[5, 1, 2, 3]]
# 얕은 복사가 되면서 안되는구나


## Deep Copy
# lst 를 a 에 할당하면 깊은복사
 a = lst[0:2]

lst = [1, 2, 3, 4]
temp = []
temp.append(lst[:])

lst.pop()
lst.insert(0, 5)

print(temp)



 # 예제
 # list 자체는 하나의 주소를 가리키고 있다
 # 2차원 이상일 경우에는, append로 안됨
 # 2차원 이상이면 import.copy 하고 copy.deepcopy....
 # 2차원 이상에서 리스트 안의 리스트 , 그리고 그 안의 원소까지 꺼내려면 위의 import.copy 이용!
 lst = [[1, 2], [3, 4]]
 temp = []
 temp.append(lst[:])

 lst[0][0] = 5
