# 목표: 정수를 받아와서 string으로 반환하기
# 일단 정수를 받아오자
# 음수일 경우, 앞에 '-'를 붙여주자
# 양수일 경우, 각 숫자를 따로따로 받아와서 거꾸로 리스트에 넣어주자

import sys

sys.stdin = open('input.txt')

def itoa(num):
    is_negative = False
    if num < 0:                         # 받아오는 정수가 음수인 경우 일단 양수로 바꿔준다
        num, is_negative = -num, True   # 그런데 이렇게 되면, return하는 값이 양수가 되므로 따로 장치를 해줘야함
    s = []
    while True:
        # ord(): 특정 문자를 아승키 코드 값으로 변환
        # chr(): 아스키 코드 값을 문자로 변환해 주는 함수
        s.append(chr(ord('0') + num % 10))
        # 숫자 시작인 0인 아스키 코드 값에다가 내가 아스키 코드를 알고 싶은 숫자를 더해주고
        # 해당 아스키 코드 값을 문자로 변환하여(chr()) 리스트에 넣어준다
        num //= 10                          # 나머지와 몫의 연산을 사용해서, 따로따로 받아준다
        if num == 0:                        # 더 이상 나눌 것이 없을 떄 loop에서 벗어남!
            break
    if is_negative:
        return '-' + ''.join(s[::-1])   # 받아오는 정수가 음수일 경우, 앞에 '-'를 붙여준다

    return ''.join(s[::-1])             # 따로 받아준게 1의 자리 숫자부터 거꾸로 받아온 것이기 때문에, 거꾸로 반환


for i in range(1, 8):
    integer = int(input())
    rlt = itoa(integer)
    print(f'#{i} {rlt} {type(rlt)}')
