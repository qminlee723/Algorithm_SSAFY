from pprint import pprint

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

pprint(num_list, width=15)

for r in range(len(num_list)):
    for c in range(len(num_list[0])):
    # 5일 때, 상하좌우에 있는 원소를 출력해보세요.
        if(num_list[r][c]) == 5:
    #         print(num_list[r-1][c]) # 상
    #         print(num_list[r+1][c]) # 하
    #         print(num_list[r][c-1]) # 좌
    #         print(num_list[r][c+1]) # 우
    #         print(num_list[r-1][c-1]) # 좌상
    #         print(num_list[r-1][c+1]) # 우상
    #         print(num_list[r+1][c-1]) # 좌하
    #         print(num_list[r+1][c+1]) # 우하

        # 델타를 이용해서 위와 같은 코드를 출력해보자
            row_d = [-1, 1, 0, 0]
            col_d = [0, 0, -1, 1]
            for d in range(4):
                each_row = r + row_d[d]
                each_col = c + col_d[d]
                print(num_list[each_row][each_col])

