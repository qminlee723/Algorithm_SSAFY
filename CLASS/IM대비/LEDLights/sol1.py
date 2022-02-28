import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     target_pattern = list(map(int, input().split()))
#
#     for i in range(1, n+2):
#         if target_pattern[1] == 1:
#             if target_pattern[i] == 1:
#                 target_pattern[i] = 0
#             else:
#                 target_pattern[i] = 1
#         if i % 2 == 0:
#             if target



TC = int(input())

for test_case in range(1, TC + 1):
    length_N = int(input())

    # led 전구의 초기값
    led = [0] * (length_N + 1)
    led_rlt = list(map(int, input().split()))


    led_rlt.insert(0, 0)
    count = 0

    for i in range(length_N + 1):
        if i == 0:
            continue
        if led[i] == led_rlt[i]:
            continue
        else:
            for j in range(i, length_N + 1):
                if j % i == 0:
                    if led[j]:
                        led[j] = 0
                    else:
                        led[j] = 1
            count += 1

        if led == led_rlt:
            print(f'#{test_case} {count}')
            break
    if led != led_rlt:
        print(f'#{test_case} error!')