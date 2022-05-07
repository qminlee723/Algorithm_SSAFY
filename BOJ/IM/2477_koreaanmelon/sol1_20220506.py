import sys
sys.stdin = open('input.txt')

K = int(input())
north = [] # 4
south = [] # 3
west = [] # 2
east = [] # 1
for i in range(6):
    direction, distance = map(int, input().split())
    # 북
    if direction == 4:
        north.append(distance)

    elif direction == 3:
        south.append(distance)

    elif direction == 2:
        west.append(distance)

    elif direction == 1:
        east.append(distance)

if len(north) == 1:
    if len(west) == 1:
        big = sum(north) * sum(west)
        small = south[1] * east[0]
        print(K*(big-small))
    elif len(east) == 1:
        big = sum(north) * sum(east)
        small = south[1] * west[0]
        print(K*(big-small))


elif len(north) > 1:
    if len(west) == 1:
        big = south[0] * west[0]
        small = north[0] * east[1]
        print(K*(big-small))
    elif len(west) > 1:
        big = south[0] * east[0]
        small = north[0] * west[1]
        print(K*(big-small))
