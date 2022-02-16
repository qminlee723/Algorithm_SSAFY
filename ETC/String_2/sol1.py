import sys

sys.stdin = open('input.txt')

def itoa(num):
    is_negative = False
    if num < 0:
        num, is_negative = -num, True
    s = []
    while True:
        s.append(chr(ord('0') + num % 10))
        num //= 10
        if num == 0:
            break
    return ''.join(s[::-1])


for i in range(1, 7):
    integer = int(input())
    rlt = itoa(integer)
    print(f'#{i} {rlt} {type(rlt)}')
