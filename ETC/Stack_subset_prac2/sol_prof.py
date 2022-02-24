
# 기본 구조는 그냥 외웁시다(모든 경우의 수를 구해줍시다)
def powerset(idx, arr):

    if idx == N:
        print(bit)
        return

    bit[idx] = 0
    powerset(idx=idx + 1, arr=arr)

    bit[idx] = 1
    powerset(idx=idx + 1, arr=arr)


lst = [x for x in range(1, 11)]
N = len(lst)
bit = [0] * N

powerset(idx = 0, arr = lst)
