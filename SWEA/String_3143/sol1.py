import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word, easy_type = input().split()

    for i in range(len(word)):
        if easy_type in word:
            # easy_type이 word안에 있는 갯수를 세 주자
            repeat = word.count(easy_type)
            # 최소 타이핑 횟수를 구해줍니다
            min_type = len(word) - len(easy_type)*repeat + repeat

    print(f'#{tc} {min_type}')