import sys

sys.stdin = open('input.txt', encoding='utf-8')

def count_pattern(pattern, text):
    cnt = 0
    i = 0
    while i < len(text):
        if text[i] == pattern[0]:
            if text[i:i+len(pattern)] == pattern:
                cnt += 1
        i += 1
    return cnt

for tc in range(1, 11):
    T = int(input())
    pattern = input()
    text = input()

    rlt = count_pattern(pattern, text)
    print(f'#{tc} {rlt}')