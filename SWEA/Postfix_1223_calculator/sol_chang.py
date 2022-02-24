import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    equation = input()

    postfix = []
    operation_stack = []
    for eq in equation:
        if eq == '*':
            operation_stack.append(eq)
        elif eq == '+':
            while operation_stack:
                postfix.append(operation_stack.pop())
            operation_stack.append(eq)
        else:
            postfix.append(eq)

    # 혹시나 남아있는게 있을까…?
    while operation_stack:
        postfix.append(operation_stack.pop())

    result = []
    for eq in postfix:
        if eq == '+':
            result.append(result.pop() + result.pop())
        elif eq == '*':
            result.append(result.pop() * result.pop())
        else:
            result.append(int(eq))

    print('#{} {}'.format(tc, *result))
