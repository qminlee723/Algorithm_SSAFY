import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()

# 반복되는 알파벳의 숫자를 세어야 하므로 cnt
    max_cnt = 0
# pattern에서 하나씩 알파벳을 뺴서 비교해준다
    for i in pattern:
# 만약 text안에 pattern의 알파벳(즉, i)가 있으면 세어주자
# 그런데 최댓값 구해줘야되므로, 그 세 준 값이 max_cnt 값보다 크면 바꿔치기
        if text.count(i) > max_cnt:
            max_cnt = text.count(i)

    print(f'#{tc} {max_cnt}')
