result = "6528-*2/+"
stack = []

for token in result:
    if token.isdigit():
        stack.append(int(token)) # token을 숫자로 바꿔줘야 함

    else:   # 연산자를 만난 경우 # p1, p2 순서 중요
        p2 = stack.pop()
        p1 = stack.pop()

        if token == "+":
            rlt = p1 + p2
            stack.append(rlt)

        elif token == "-":
            rlt = p1 - p2
            stack.append(rlt)

        elif token == "*":
            rlt = p1 * p2
            stack.append(rlt)

        elif token == "/":
            if p2 == 0:
                print('To infinity and beyond!')
            rlt = p1 / p2
            stack.append(rlt)

ans = stack.pop()
print(ans)


# p2 가 0일 때 등