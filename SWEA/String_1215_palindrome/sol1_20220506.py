import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    words = [list(input()) for _ in range(8)]

    # 가로 확인
    cnt = 0
    for i in range(8):
        # 아니 근데 이런 범위 같은거 일일히 디버깅 해보지 않고는 이게 잘못된건지 아닌지 잘 모르겠는데
        # 하 ...
        for j in range(8-length+1):
            if words[i][j:j+length] == words[i][j:j+length][::-1]:
                cnt += 1

    # transpose
    # 이렇게 하는 방법이 있는거 알았는데
    # 기억이 안나서 zip 검색 좀 했습니다
    words_col = list(map(list, zip(*words)))

    # # 세로확인
    for i in range(8):
        for j in range(8-length+1):
            if words_col[i][j:j+length] == words_col[i][j:j+length][::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')