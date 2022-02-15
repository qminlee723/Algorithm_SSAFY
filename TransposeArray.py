A = [1, 2, 3]
bit = [0] * 3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            # print(bit)
            for p in range(3):
                if bit[p]:
                    print(A[p], end=' ')
            print()
            # 빈 줄 하나 = 공집합이므로 총 8개 맞음!(2^3)