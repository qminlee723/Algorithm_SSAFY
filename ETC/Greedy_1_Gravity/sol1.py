import sys

sys.stdin = open('input.txt')

# number of Test Case
T = int(input())

##### for box in range에서의 box와 boxen을 첨에 똑같이 이름을 줘서 넘버링이 제대로 안 나옴
#### 밑줄이 생기는 데는 다 이유가 있다!
for box in range(1, T+1):
    # length of box
    block = int(input())
    # 박스 하나 하나를 정수로 받은 다음에 리스트에 추가
    boxen = list(map(int, input().split()))


    # 중력 작용시 떨어지는 낙차가 가장 큰 박스의 낙차 크기를 구하시오
    # 제일 처음에 있는 박스(i)와 같거나 큰 박스가 있다면 그만큼 count를 세면서 낙차 크기 기록
    # 제일 처음에 있는 박스를 hold 하면서 다른 걸 계속 비교해야되니까 nested for loop
    max_v = 0

    for i in range(len(boxen)):
        cnt = 0
        for j in range(i+1, len(boxen)):
            ######### 박스i와 같거나 큰 박스가 있으면, ====> 박스 i보다 작은 박스가 있어야 공간이 생김
            ######### cnt는 빈 공간을 카운트 하는거임!!!! 부등호 방향 조심
            if boxen[i] > boxen[j]:
                # cnt를 올려준다
                cnt += 1
        # max_v 의 값보다 cnt가 더 크면, cnt가 새로운 max_v가 된다
        if cnt >= max_v:
            max_v = cnt

    print(f'#{box} {max_v}')

