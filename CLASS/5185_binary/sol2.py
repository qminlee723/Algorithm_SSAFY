import sys
sys.stdin = open('input.txt')

def BinaryNum(N, lst): # 2진수 구하는 함수
    intN = int(N)
    # a = intN // 2  # 어디까지 나눠야되는지 알아야되니까 2를 나눔
    # b = intN % 2   # 나머지들이 곧 이진수가 되니까 이걸 저장해야겠다
    a, b = divmod(intN, 2)
    lst.append(b) # 이걸 쭉 이으면 이진수가 됩니다
    if a == 0:  # 주어진 숫자를 2로 나눌 수 있을 때 까지 나누면
        return lst
    else:
        return BinaryNum(a, lst) # 아직 a가 남아있으면 몫/나머지 처리 계속 반복


T = int(input())

P = {
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15'
}

for tc in range(1, T+1):
    N, hex = map(str, input().split())

    h_lst = []
    # 먼저 문자를 숫자로 변환
    for h in hex:
        if h in P:
            h = P[h]
            h_lst.append(h)
        else:
            h_lst.append(h)

    a = ''.join(h_lst)
    lst = []
    rlt = BinaryNum(int(a), lst)

    rlt_lst = []
    for r in rlt:
        rlt_lst.append(str(r))
        ans = ''.join(rlt_lst)
    print(f'#{tc} {ans}')