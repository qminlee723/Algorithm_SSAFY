
# 기본 구조는 그냥 외웁시다(모든 경우의 수를 구해줍시다)
# arr은 없어도 괜찮습니다 왜냐면 밑에 주어지는 것들이 global이므로
def powerset(idx, arr):
    # 예???????????
    # 가지치기 했을 때 얼마나 줄어드는지 확인
    global cnt
    cnt += 1


    # 합의 계산
    # 만약 이번에 들어왔는데, 부분집합의 합이 10 이면 return
    each_sum = 0
    for each in zip(bit, lst):  # each: (1, 2), (1, 4) ...
        each_sum += each[0] * each[1]

    if each_sum == 10:
        for each in zip(bit, lst):
            if each[0]:
                print(f"{each[1]}", end = "")
        # print(lst)  # 10진수
        # print(bit)  # 2진수 ==> 1이 가리키는 숫자들의 합이 10이면 성공!
        print()
        return

    # each_sum > 10 넣어준 것이 백트래킹
    # 가지치기(연산 수 줄어듦)
    elif each_sum > 10:
        return

    if idx == N:
        # print(bit)
        return

    bit[idx] = 1
    powerset(idx=idx + 1, arr=arr)

    bit[idx] = 0
    powerset(idx=idx + 1, arr=arr)


cnt = 0
lst = [x for x in range(1, 11)]
N = len(lst)
bit = [0] * N

powerset(idx = 0, arr = lst)
print(f"cnt {cnt}")
