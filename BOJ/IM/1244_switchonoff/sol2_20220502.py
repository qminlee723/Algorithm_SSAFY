import sys
sys.stdin = open('input.txt')


switch_num = int(input())
# 인덱싱 편의를 위해
on_off = [2] + list(map(int, input().split()))
student_num = int(input())

def onoffswitch(index):
    if on_off[index] == 1:
        on_off[index] = 0
    elif on_off[index] == 0:
        on_off[index] = 1


for _ in range(student_num):
    gender, ass_n = map(int, input().split())

    # 남학생의 경우
    if gender == 1:
        for i in range(ass_n, switch_num+1, ass_n):
            onoffswitch(i)

    # 여학생의 경우
    if gender == 2:
        onoffswitch(ass_n)
        # 어디까지 대칭이 되는지를 찾아야 함
        for i in range(switch_num//2):
            if 0 < ass_n - i and ass_n + i <= switch_num:
                if on_off[ass_n - i] == on_off[ass_n + i]:
                    onoffswitch(ass_n-i)
                    onoffswitch(ass_n+i)
                else:
                    break

for j in range(1, switch_num+1):
    print(on_off[j], end=' ')
    if j % 20 == 0:
        print()
