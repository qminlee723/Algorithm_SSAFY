# 1. dictionary 를 이용해서 실제 크기를 알아낸다.
# 2. 내가 알고 있는 알고리즘을 이용해서 정렬하기
# 3. 출력하기
# 단, 개수 세서 개수 만큼 반복하며 출력하는거 하지 말기
# 7시 15분까지 개인 으로 풀이
GNS_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2,
            'THR': 3, 'FOR': 4, 'FIV': 5,
            'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}


# target = ['SVN', 'FOR' ,'ZRO', 'NIN', 'FOR', 'EGT', 'EGT', 'TWO']
def bubble_sort(target, N):
    # 1.  모든 요소 2개씩 비교 큰 것을 뒤로 보내기 > 작업 한번하면 제일 큰수가 제일 뒤로 갑니다.
    # 1번작업을 요소의 개수 만큼 반복하면 정렬됨
    for j in range(N - 1):
        for i in range(N - 1 - j):
            if GNS_dict[target[i]] > GNS_dict[target[i + 1]]:
                target[i], target[i + 1] = target[i + 1], target[i]


def select_sort(target, N):
    # 1. 제일 작은거 찾아와서 제일 앞에 넣기
    # 2. 반복할 때마다 그 다음 작은거 찾아서 그 뒤에 넣어주기
    for i in range(N - 1):  # i번째 자리에 들어갈 요소 찾기
        min_idx = i
        for j in range(i + 1, N):
            if GNS_dict[target[j]] < GNS_dict[target[min_idx]]:
                min_idx = j
        target[i], target[min_idx] = target[min_idx], target[i]


def counting_sort(target, N):
    # 각 숫자들이 몇개 나왔는가...세야 합니다..0~9
    count = [0] * 10
    new_arr = [''] * N
    # 각 숫자들이 몇개 나왔는지 개수 세기
    for i in range(N):
        count[GNS_dict[target[i]]] += 1
    # 누적합 구해서 각 숫자들이 어느자리에 들어가는지 계산
    for i in range(1, 10):
        count[i] += count[i - 1]
    # 누적합 제대로 구했으니까....
    # target 거꾸로...돌아서 집어넣어도 되고...그냥 앞에서 해도 됩니다.
    # 동일 가치 원소에 대한 입력 순서를 지키고 싶을 때는 뒤에서 부터 읽으면 됩니다.
    for i in range(N):
        count[GNS_dict[target[i]]] -= 1
        new_arr[count[GNS_dict[target[i]]]] = target[i]
    return new_arr

import sys
sys.stdin = open('input.txt')

# target = ['SVN', 'FOR' ,'ZRO', 'NIN', 'FOR', 'EGT', 'EGT', 'TWO']
# bubble_sort(target,8)
# select_sort(target,8)
# print(counting_sort(target,8))
# print(target)

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    target = input().split()
    # bubble_sort(target,N)
    result = counting_sort(target, N)
    print(tc, *result)