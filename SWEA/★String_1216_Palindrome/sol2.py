# 창환이 풀이
for _ in range(1, 11):
    T = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    arr2 = list(zip(*arr))
    max_count = 1

    for i in range(N, 1, -1):
        if max_count >= i:
            break
        for j in range(N - i + 1):
            if max_count == i:
                break

            # for elem1, elem2 in zip(arr, arr2):
            # target1 = elem1[j:j+i]
            # target2 = elem2[j:j+i]

            # if target1 == target1[::-1] or target2 == target2[::-1]:
            #     max_count = i
            #     break

            # 윗 방법이 제일 좋은 방법
            # 밑에 방법이 풀어쓴거

            for elem in arr:
                target = elem[j:j + i]
                if target == target[::-1]:
                    if max_count <= i:
                        max_count = i
                        break

            for elem in arr2:
                target = elem[j:j + i]
                if target == target[::-1]:
                    if max_count <= i:
                        max_count = i
                        break

    print("{} {}".format(T, max_count))