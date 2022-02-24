import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    result = input().split()

    # create stack for nums
    stack = []
    for token in result:
        # token이 숫자인 경우, append
        if token.isdigit():
            stack.append(int(token))

        # token 이 연산자인 경우,
        else:

            if token == '+':
                if len(stack) > 1:          # stack에 든 숫자가 2 이상이면
                    p2 = stack.pop()
                    p1 = stack.pop()
                    rlt = p1 + p2           # 해당 연산을 해서
                    stack.append(rlt)       # stack에 append
                else:
                    print(f'#{tc} error')   # stack이 비어있거나, 1이면 error
                    break

            elif token == '-':
                if len(stack) > 1:
                    p2 = stack.pop()
                    p1 = stack.pop()
                    rlt = p1 - p2
                    stack.append(rlt)
                else:
                    print(f'#{tc} error')
                    break

            elif token == '*':
                if len(stack) > 1:
                    p2 = stack.pop()
                    p1 = stack.pop()
                    rlt = p1 * p2
                    stack.append(rlt)
                else:
                    print(f'#{tc} error')
                    break

            elif token == '/':
                if len(stack) > 1:
                    p2 = stack.pop()
                    p1 = stack.pop()
                    rlt = p1 // p2
                    stack.append(rlt)
                else:
                    print(f'#{tc} error')
                    break

            elif token == '.':              # token 이 . 이면
                if len(stack) == 1:         # stack에 하나의 결과만 남아 있을 때
                    print(f'#{tc} {rlt}')   # 결과를 반환한다
                else:
                    print(f'#{tc} error')   # 숫자가 stack에 남아 있거나, 비었으면 error

