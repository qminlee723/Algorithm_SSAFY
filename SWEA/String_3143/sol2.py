# 교수님 풀이

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):

    a_str, b_str = input().split()
    typing = a_str.split(b_str)
    typing = "x".join(typing)
    print(f"#{tc} {len(typing)}")
