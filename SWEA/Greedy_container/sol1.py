import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N = 컨테이너 수,  M = 트럭 수
    N, M = map(int, input().split())
    # N개의 화물 무게
    wi = list(map(int, input().split()))
    # M개의 적재용량
    ti = list(map(int, input().split()))

    # 옮겨갈 수 있는 총 무게. 갱신되면 안되니까 for 문 밖으로 빼준다.
    total_lst = []

    # 트럭 수가 기준이 되어야 하니까
    for i in range(M):
        lst = []
        for j in range(len(wi)):
            # 만약 트럭 적재용량이 컨테이너 무게보다 크면, 후보군에 넣게 리스트에 넣어주자
            # 그런데 이 리스트는 트럭 한 대 찰 때 마다 갱신되어야 하므로 for 문 안에 넣어준다
            if ti[i] >= wi[j]:
                lst.append(wi[j])
        # 리스트를 일단 완성시키고 나서 최댓값을 구해줍니당
        # 자 여기서 그럼 문제가 생기는데, 쭉 돌다보면 준비된 트럭 용량이 다 엄청 크면 이미 실어간 컨테이너도 또 실을수 있게 됨
        # 이런 중복을 막으려면 어떻게 해야 할지 생각을 해봐야 하겠는데... 노가다를 해보자면...

        # 리스트가 안 비어있으면,
        if lst:
            # 리스트 중에서 최댓값 빼오기
            max_value = max(lst)
            # 최댓값을 더해줄 리스트에다가 추가(걍 total=0 해도 됐으려나..?)
            total_lst.append(max_value)
            # 넣어준 값은 wi에서 빼서 중복 없애주자
            wi.remove(max_value)


    print(f'#{tc} {sum(total_lst)}')
