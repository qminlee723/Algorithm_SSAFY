import sys

sys.stdin = open('input.txt')

def check_babygin(numbers):
    counter = [0]*10            # 각 숫자를 카운트 할 리스트
    is_babygin = 0              # 정답 여부

    # 0부터 9의 카드 갯수 세기
    for number in numbers:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        if idx < len(counter)-2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                counter[idx] -= 1
                counter[idx + 1] -= 1
                counter[idx +2] -= 1
                is_babygin += 1
                continue

        if is_babygin == 2:
            return 1
        idx += 1

    return 0




T = int(input())

for tc in range(1, T + 1):

    numbers = list(map(int, input()))
    result = check_babygin(numbers)

    print(f'#{tc} {result}')
