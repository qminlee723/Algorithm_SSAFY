import sys

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

queue = []
for n in range(1, N + 1):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        queue.append(word[1])

    elif word[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif word[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif word[0] == 'size':
        print(len(queue))

    elif word[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif word[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])