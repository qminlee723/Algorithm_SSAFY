import sys
sys.stdin = open('input.txt')

# 쭉 그려보니 0 1 1 3 2 는 인덱스 값
# 그런데 앞, 뒤가 통상적으로 생각하는 리스트의 앞뒤가 아니어서 reverse 해줌

N = int(input())
queue = list(map(int, input().split()))

new_q = []
student = 1
for i in queue:
    new_q.insert(i, student)
    student += 1
new_q.reverse()

for q in new_q:
    print(q, end=' ')