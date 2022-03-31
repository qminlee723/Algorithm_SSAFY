def hoare(A, 1, r):
    p = A[1]
    i, j = 1, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[i] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[1]
    return j

def qsort(A, 1, r):
    if 1 < r:
        s = hoare(A, 1, r)
        qsort(A, 1, s - 1)
        qsort(A, s + 1, r)
# A = [7, 2, 5, 3, 1, 4, 1]
# A = [1, 2, 3, 4, 5, 6, 7]
# A = [7, 6, 5, 4, 3, 2, 1]

A = [7, 1, 1, 1, 7]
N = len(A)
qsort(A, 0, N-1)
print(A)

