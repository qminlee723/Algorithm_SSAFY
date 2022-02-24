# 이 구조는 외웁시다
# 직접 손으로 쓰면서 for문을 돌려봅시다 

def perm(i):
    if i == len(p):
        print(p)
    else:
        for j in range(i, len(p)):
            p[i], p[j] = p[j], p[i]
            perm(i + 1)
            p[i], p[j] = p[j], p[i]
            perm(i + 1)

p = [1, 2, 3]

perm(0)