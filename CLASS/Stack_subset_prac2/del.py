def powerset(idx, N):

    if idx == N: # 종료조건
        print(bit)
        return

    bit[idx] = 1
    powerset(idx + 1, N)

    bit[idx] = 0
    powerset(idx + 1, N)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(a)
bit = [0] * N

powerset(idx=0, N=N)