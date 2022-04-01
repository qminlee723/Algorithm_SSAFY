import sys

sys.stdin = open('input.txt')


def partition(num, start, end):
    pivot = num[start]  # pivot설정
    left = start + 1
    right = end
    done = False

    while not done:
        # left가 기리키는 값과 pivot값을 비교해서 더 작은 경우 left 값을 증가
        # pivot 값보다 큰데 좌측에 있는 값을 찾기 위해서임
        # pivot 값보다 작으면 제대로 있는거니까 left를 증가시켜 다음꺼 확인해주는 과정
        while left <= right and num[left] <= pivot:  # left 계속 증가시킨다
            left += 1
        # pivot값보다 큰 값이 오른쪽에 있는 경우도 제대로 있는 거
        # 그러니까 right 증가시켜서 다음값도 제대로 있는지 확인해준다
        while left <= right and pivot <= num[right]:  # right 계속 감소시킨다
            right -= 1
        if right < left:  # 언제까지?
            done = True  # left, right 교차할때까지
        # 값이 제 자리를 찾지 못한 경우(큰 값이 왼쪽에 있거나, 작은 값이 오른쪽에 있는 경우)
        else:
            num[left], num[right] = num[right], num[left]  # 둘이 자리바꿔준다

        # 여기서 right이 가리키는 값은 pivot 오른쪽에서 피봇보다 작은 작은 값일 테니까
        # pivot과 right을 바꾸어 주고, right 값을 pivot으로 바꿔줍니다.
    num[start], num[right] = num[right], num[start]
    # pivot이 될 값을 반환
    ####### 여기서 왜 right이 pivot이 되는지 뭔가 확실히 설명을 못하겠음 ###########
    return right


def quick_sort(num, start, end):  # (리스트, 출발, 도착)
    if start < end:  # 만약 start가 end보다 작으면(즉 교차X)
        pivot = partition(num, start, end)  # pivot을 설정해준다
        quick_sort(num, start, pivot - 1)
        quick_sort(num, pivot + 1, end)
    return num


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    # N개의 정수를 정렬해 리스트 A에 넣고
    A = quick_sort(num, 0, len(num) - 1)
    # A[N//2]에 저장된 값을 출력
    print('#{} {}'.format(tc, A[N // 2]))