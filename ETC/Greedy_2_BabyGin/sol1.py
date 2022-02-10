import sys

sys.stdin = open('input.txt')

# Test Case 갯수
T = int(input())

# Test Case 갯수가 9개인걸 알고 있으니 T + 1 만큼의 빈 array 를 만들어 줍니다


for num in range(1, T + 1):
    # 6자리 숫자를 정수로 받아줍니다
    n = int(input())
    arr = [0] * 10

    for i in range(6):
        # 오른쪽 숫자부터 하나하나 떼 내 주고, 이를 array에다 담아줍니다
        # 그 array에서 자신의 크기를 인덱스로 갖습니다
        # 그 array[i]에 동일한 숫자가 들어오면 1을 더해줍니다
        arr[n % 10] += 1
        # 이 작업이 끝나면, 처리가 끝난 마지막 자리 숫자를 뺀 다섯 자리 숫자를 받아내고 반복합니다.
        n //= 10

    # array 완성!
    # 이제 triplet 과 run을 판별합니다
    # triplet 판단

    j = 0
    cnt = 0
    while j < 10:
        if arr[i] >= 3:
            arr[i] -= 3
            cnt += 1
            continue

        if i > 7:
            print(f'#{num} 1')



        # run 판단
        # IndexError 나서 arry를 12로 바꾸라는 거임
        # 근데 나는 저 위에서 i > 7 줬는데 왜 남?

        if arr[i] and arr[i+1] and arr[i+2] >= 1:
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            cnt += 1
            continue
        j += 1

    # baby gin 판단
    if cnt >= 2:
        print(f'#{num} 1')
    else:
        print(f'#{num} 0')


