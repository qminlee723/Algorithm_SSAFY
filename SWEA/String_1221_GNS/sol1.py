# 일단 key value로 이루어진 dictionary를 만들어서
# input을 key 로 지정 후,
# 만들어진 dictionary에서 순차적으로 그 값을 빼 온다
# 그리고 그 값들을 새로운 리스트에 넣어주고
# 해당 리스트를 작은 수부터 차례로 정렬한다
#
# 일단 정렬하기 위해서 bubble sort를 구현한다

import sys

num_dict = dict(ZRO=0, ONE=1, TWO=2, THR=3, FOR=4, FIV=5, SIX=6, SVN=7, EGT=8, NIN=9)
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if num_dict[arr[j]] > num_dict[arr[j+1]]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    num_char, n = input().split()
    number_system = list(input().split())
    sorted_value = bubble_sort(number_system)
    print(sorted_value)