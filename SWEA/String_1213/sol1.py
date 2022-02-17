# 목표: 랜덤한 text 안에서 pattern이 얼마나 반복되는지 카운트
import sys

sys.stdin = open('input.txt', encoding='utf-8')

def count_pattern(pattern, text):
    # 패턴이 나올 때 마다 카운트 해줘야하므로 카운트 할 변수를 지정
    cnt = 0
    i = 0
    # text를 쭉 돌면서 확인해야하므로 loop을 돌림
    while i < len(text):
        # 확인해야 하는 text의 인덱스가 패턴의 길이와 같아야 하므로, 슬라이싱을 이용
        if text[i] == pattern[0]:   # 만약 텍스트 속 알파벳이 패턴의 첫 알파벳과 일치하는 경우
            if text[i:i+len(pattern)] == pattern: # 나머지도 일치하는지 확인하고
                cnt += 1                          # 일치 시 카운트
        i += 1
    return cnt

for tc in range(1, 11):
    T = int(input())
    pattern = input()
    text = input()

    rlt = count_pattern(pattern, text)
    print(f'#{tc} {rlt}')