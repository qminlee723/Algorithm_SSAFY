import sys

sys.stdin = open('input.txt')
#
# # 문자열 뒤집기
# # 1. 슬라이싱 사용
# T = int(input())
# for tc in range(1, T+1):
#     words = input()
#
#     print(f'#{tc} {words[::-1]}')
#
#
# # 2. reverse 메소드를 사용하고싶다
# T = int(input())
# for tc in range(1, T+1):
#     words = list(input())
#     words.reverse()
#     words = "".join(words)
#
#     print(f'#{tc} {words}')


# 3. 새로운 문자열 생성
T = int(input())

for tc in range(1, T+1):
    words = input()

    backword = ""
    for word in words:
        backword = word + backword
    print(f'#{tc} {backword}')


