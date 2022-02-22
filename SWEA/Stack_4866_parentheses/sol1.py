import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = input()

    result = 1                                          # 디폴트값으로 1을 준다(1 = 성공!)
    stack = []
    for i in range(len(n)):
        # 여는 괄호를 발견하면, 체크박스에 넣어준다
        if n[i] == '(' or n[i] == '{':
            stack.append(n[i])

        elif n[i] == ')':                               # 닫는 소괄호를 찾으면
            if len(stack) > 0 and stack[-1] == '(':     # stack에 내용이 있고, 가장 마지막에 넣은 괄호가 (이면
                stack.pop()                             # 저장되어 있던 여는 소괄호를 없앤다
            else:
                result = 0                              # 닫는 소괄호를 찾았는데, 내용이 없거나
                break                                   # 마지막에 넣은 괄호가 여는 소괄호이면 0(실패)출력후 break

        elif n[i] == '}':                               # 중괄호에 대해서도 같은 방법으로 찾아준다
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break


    if len(stack) != 0:                                 # 만약
        result = 0

    print(f'#{tc} {result}')


# 1. or 과 and : or 의 경우 하나만 맞아도 T, and는 둘 다 만족해야 T.
# 2. indentation: 어디서 조건문이 끝나는지를 확실히 보자.
# 3. 괄호가 닫힐 때 (는 )와, {는 }와 함께 닫혀야 하는 것을 확인해주자
# 4. 런타임 에러 =  break를 통해 불필요한 연산 줄이자
# 5. 무엇을 출력하는지 생각하자(result 대신 1, 0 출력하고있었음;)