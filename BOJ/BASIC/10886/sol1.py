N = int(input())

data = []
for _ in range(N):
    survey = int(input())
    data.append(survey)

    notcute = data.count(0)
    cute = data.count(1)

    if notcute > cute:
        print('Junhee is not cute!')
    else:
        print('Junhee is cute!')