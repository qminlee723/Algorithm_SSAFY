import sys
sys.stdin = open('input.txt')

T = 1
for tc in range(1, 11):
    dump_cnt = int(input())
    height = list(map(int, input().split()))

    # while dump_cnt > 0:
    #     dump_cnt -= 1
    for dump in range(dump_cnt):
        for i in range(100):
            if height[i] == max(height):
                height[i] -= 1
                for j in range(100):
                    if height[j] == min(height):
                        height[j] += 1
                        break
                break
    ans = max(height) - min(height)
    print(f'#{tc} {ans}')