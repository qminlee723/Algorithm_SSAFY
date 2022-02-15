import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
double_que = []

for n in range(1, N + 1):
    word = sys.stdin.readline().split()

    if word[0] == 'push_front':
        double_que.insert(0, word[1])

    elif word[0] == 'push_back':
        double_que.append(word[1])

    elif word[0] == 'pop_front':
        if len(double_que) == 0:
            print(-1)
        else:
            print(double_que.pop(0))

    elif word[0] == 'pop_back':
        if len(double_que) == 0:
            print(-1)
        else:
            print(double_que.pop())

    elif word[0] == 'size':
        print(len(double_que))

    elif word[0] == 'empty':
        if len(double_que) == 0:
            print(1)
        else:
            print(0)

    elif word[0] == 'front':
        if len(double_que) == 0:
            print(-1)
        else:
            print(double_que[0])

    elif word[0] == 'back':
        if len(double_que) == 0:
            print(-1)
        else:
            print(double_que[-1])