from pprint import pprint
#1. 5 * 5 matrix 초기화 하기
matrix = []
for i in range(5):
    row = [j + i * 5 for j in range(1, 6)]
    matrix.append(row)


rlt = 0
#2. 각각의 요소의 차 구하기
#2-1. 각각의 요소에 접근하기
for r in range(len(matrix)):
    for c in range(len(matrix)): # delta를 이용한 상하좌우 접근
        d_row = [-1, 1, 0, 0]
        d_col = [0, 0, -1, 1]
        for d in range(4):
            each_row = r + d_row[d]
            each_col = c + d_col[d]

            # 범위 체크 해주세여 (IndexError)
            if each_row < 0 or each_row > 4 or each_col < 0 or each_col > 4:
                continue
            else:
                print(f'target {matrix[r][c]} -> {matrix[each_row][each_col]}')
                # 각 요소의 차 구하기
                sub = matrix[r][c] - matrix[each_row][each_col]
                # 절대값 처리하기(feat.삼항연산자)
                sub = sub if sub >= 0 else -sub
                # 합 누적하기
                rlt += sub

print(rlt)