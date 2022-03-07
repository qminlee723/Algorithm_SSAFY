import sys
import math

sys.stdin = open('input.txt')

while True:
    try:
        # split
        a, b = input().split()
    except:
        # split 한 값이 없을때 break
        break
    # 일단 output 요구사항 맞추기 a b = result format
    print(f"{a} {b} = ", end='')
    # 해당 문자열로 만들 수 있는 모든 경우의 수 찾기 factorial
    fact = math.factorial(len(a))
    # 모듈러(%)를 사용하기 위해서 -1 해줌 0부터 index 할거임 * 1-1
    b = int(b) - 1
    # 만약에 b가 모든 경우의수보다 큰 숫자가 들어올때는 수열 찾을 수 없음
    # No Permutation print 하고 다음 input 으로 넘어감
    if fact <= b:
        print("No permutation")
        continue

    # 수열 담을 result 초깃값 설정
    result = ''
    # a가 남아 있으면 계속 돌거임 수열을 만들어야 하니까
    while len(a) > 0:
        # 선택된 첫번째 자리가 가질 수 있는 경우의 수 찾기 예) abcd 4! = 24 인데 각 자리 마다 6개의 size 를 가진 4개의 집합으로 만들어짐
        # 즉, 24 // len(a)를 하게 되면, 24 // 4 = 6가지의 경우의 수를 가지는걸 알 수 있음
        #  a -> 6가지 수열 가지게 되고 b -> 6가지 수열을 가지게 됨
        fact //= len(a)
        # 그럼 24개의 경우의 수 중에 17번째 (16임 0부터 셀거라서 1-1 참고) 를 알아야함.
        # 그래서 16 // 6 (각자리의 경우의수) 를 하게 되면
        # 그러면 2 -> 첫번째 자리가 됨 a[2] -> c
        index = b // fact
        # a[2] 를 result에 담아줌
        result += a[index]
        # a[2] 를 a 에서 제외 시킴
        a = a[:index] + a[index + 1:]
        # 이제 그 다음 자릿수를 구해야 하는데,정해진 집합에서 (2번째 집합)  16번째 % 6(경우의수) = 4 (4번째 자리를 찾아야 하는걸 정해줌)
        b %= fact
        # 반복함
    print(result)