import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input())) # 띄어쓰기 없는 정수를 리스트로 받아온다

    # 0에서 9까지 숫자가 적힌 N장의 카드가 주어질 떄,
    # 가장 많은 카드에 적힌 숫자와
    # 카드가 몇 장인지 출력하라.
    # 단, 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

    # 중복 카드 갯수 셀 리스트 생성
    # 0~9까지라고 했으니 10개 넣어줄 빈 리스트 만든다
    card_set = [0] * 10

    # 하나하나 보면서 본인 크기만큼의 리스트 인덱스에 추가하자
    # 추가될 때마다 1씩 더해짐
    for i in ai:
        card_set[i] += 1

    # 추가된 값 중 가장 큰 값을 구한다
    # 그럼 일단 아까 만든 리스트(card_set)를 loop 돌리면서 큰 값을 찾아봐야 함
    # max 값 저장할 변수가 필요함!
    # 그리고 그 큰 값을 가지는 카드의 숫자도 구해야 함 => 변수 지정 필요!
    max_cnt = 0
    max_num = 0
    for j in range(len(card_set)):
        if card_set[j] >= max_cnt:
            max_cnt = card_set[j]
            max_num = j

    print(f'#{tc} {max_num} {max_cnt}')

