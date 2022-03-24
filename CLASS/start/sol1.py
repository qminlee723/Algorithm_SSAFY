import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
# 0 ~ 9까지의 수와 대응하는 이진 코드
    N, M = map(int, input().split())
    P = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    bits = []
    for _ in range(N):
        a = input()

        idx = 0
        if bits:
            continue
        while idx < M-7:
            idx += 1
            if a[idx:idx+7] in P and not int(a[idx + 7]):
                bits.append(P[a[idx:idx+7]])
                idx += 6
    if not (sum(bits) + 2 * sum(bits[0:7:2])) % 10:
        ans = sum(bits)
    else:
        0
    print(f'#{tc} {ans}')