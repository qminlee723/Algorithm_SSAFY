import sys
sys.stdin = open('input.txt')

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

# 절대 뒤에 붙을 수 없는 숫자는 반대편에 있는 숫자임
# 0, 5
# 1, 3
# 2, 4
# 각각의 경우의 수 제외하고 하나하나 붙여본 다음에 최댓값 구하면 될 것 같음


