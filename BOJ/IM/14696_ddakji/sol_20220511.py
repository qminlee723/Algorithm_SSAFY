import sys
sys.stdin = open('input.txt')

# 별 동그라미 네모 세모
# 4 3 2 1

game_round = int(input())
for _ in range(game_round):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if A[1:len(A)].count(4) > B[1:len(B)].count(4):
        print('A')
    elif A[1:len(A)].count(4) < B[1:len(B)].count(4):
        print('B')
    elif A[1:len(A)].count(3) > B[1:len(B)].count(3):
        print('A')
    elif A[1:len(A)].count(3) < B[1:len(B)].count(3):
        print('B')
    elif A[1:len(A)].count(2) > B[1:len(B)].count(2):
        print('A')
    elif A[1:len(A)].count(2) < B[1:len(B)].count(2):
        print('B')
    elif A[1:len(A)].count(1) > B[1:len(B)].count(1):
        print('A')
    elif A[1:len(A)].count(1) < B[1:len(B)].count(1):
        print('B')
    else:
        print('D')

