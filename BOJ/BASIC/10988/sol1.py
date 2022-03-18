word = list(input())

if word == word[::-1]:
    print(1)
else:
    print(0)


while True:
    a, b = map(int, input().split())
    print(a + b)

