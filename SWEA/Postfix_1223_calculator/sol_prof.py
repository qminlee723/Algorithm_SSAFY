infix = "(6+5*(2-8)/2)"
stack = [] # 변환을 위해 사용할 스택
result = [] # 결과가 담길 스택

# 1. 중위 표현식을 순회해야 한다.

for token in infix:

    # 2. 만약, 너 숫자면 result에 push
    if token.isdigit():
        result.append(token)

    else: # 3. 연산자일 경우,
        if not stack:   # 스택에 비었으면
            stack.append(token)
        else: # 스택이 비어있지 않다면(icp, isp 비교해서 push)

            ### 이부분이 제일 중요!! icp isp 비교 ###
            ### 큰 것부터 처리를 하자!
            # icp == 3 일 때,
            if token == '(':
                stack.append(token)
            elif token == ')': # TEMP 부분 이해 안감 ###########
                temp = stack.pop()
                while temp != '(':
                    result.append(temp)
                    temp = stack.pop()

            # icp == 2 일 때,
            elif token == '*' or token == '/':
                # 왜냐면 얘네가 가장 높은 icp일 테니까
                while stack and stack[-1] == '*' or stack[-1] == '/':
                    result.append(stack.pop())
                stack.append(token)

            # icp == 1 일 때,
            elif token == '+' or token == '-':
                while stack and stack[-1] != '(': # 다 걸렀으니까 따로 비교해 줄 필료 없음
                    result.append(stack.pop())
                stack.append(token)


# 만약, 스택에 남아있다면 모두 꺼내서 push
for token in range(len(stack)):
    result.append(stack.pop())

print(infix)
print(result)