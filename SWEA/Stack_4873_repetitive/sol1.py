import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = input()


    stack = []                          # stack 만들기
    for i in range(len(s)):
        if len(stack) == 0:             # stack이 비어 있으면  s안의 알파벳 넣어주기
            stack.append(s[i])
        elif s[i] != stack[-1]:         # stack안의 문자와 s 안의 문자가 다르면
            stack.append(s[i])          # 스택에 넣어줍니당
        else:
            stack.pop()                 # 같으면 넣지말고, 스택 안에 있는것도 지워줍니다. 반복!

    print(f'#{tc} {len(stack)}')

