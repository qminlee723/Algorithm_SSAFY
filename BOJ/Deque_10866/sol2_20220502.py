import sys
sys.stdin = open('input.txt')

N = int(input())
double_que = []

for n in range(N):
    command = input().split()

    if command[0] == 'push_front':
        double_que.insert(0, command[1])

    elif command[0] == 'push_back':
        double_que.append(command[1])

    elif command[0] == 'pop_front':
        if double_que:
            print(double_que.pop(0))
        else:
            print(-1)

    elif command[0] == 'pop_back':
        if double_que:
            print(double_que.pop())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(double_que))

    elif command[0] == 'empty':
        if double_que:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if double_que:
            print(double_que[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if double_que:
            print(double_que[-1])
        else:
            print(-1)



