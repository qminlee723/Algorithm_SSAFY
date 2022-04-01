# 1. 경유지를 다 거친 다음에 전체비용 계산하는 방법

# def nPr(i, N, s):
#     global minV
#
#     if i == N:
#         s += arr[p[N-1]][0]
#         if minV > s:
#             minV = s
#     elif s >= minV
#         return
#     else:
#         for j in range(i, N):
#             p[i], p[j] = p[j], p[i]
#             nPr(i+1, N, s + arr[p[i-1]][p[i]])
#             p[i], p[j] = p[j], p[i]
#     return


# 2. 경유지가 결정이 될 때마다 비용을 계산하는 방법 ( = sol1 침고)
