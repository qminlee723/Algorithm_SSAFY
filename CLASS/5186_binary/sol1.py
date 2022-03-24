import sys
sys.stdin = open('input.txt')

def BinaryNum(N): # 2진수 구하는 함수
    a = N // 2  # 어디까지 나눠야되는지 알아야되니까 2를 나눔
    b = N % 2   # 나머지들이 곧 이진수가 되니까 이걸 저장해야겠다
    lst.append(b) # 이걸 쭉 이으면 이진수가 됩니다
    if a == 0:  # 주어진 숫자를 2로 나눌 수 있을 때 까지 나누면
        if len(lst) > 13:
            return 'overflow'
        else:
            return lst
    else:
        return BinaryNum(a) # 아직 a가 남아있으면 몫/나머지 처리 계속 반복


T = int(input())

for tc in range(1, T+1):
    N = float(input())
    lst = []
    ans = BinaryNum(N)
    print(f'#{tc} {ans}')