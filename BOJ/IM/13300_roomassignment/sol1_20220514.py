import sys
sys.stdin = open('input.txt')

female = []
male = []
total_num, max_cap = map(int, input().split())

for i in range(total_num):
    student = list(map(int, input().split()))
    if student[0] == 0:
        female.append(student[1])
    elif student[0] == 1:
        male.append(student[1])

ans = 0
for j in range(1, 7):
    if female.count(j) > 0:
        if female.count(j) <= max_cap:
            ans += 1
        elif female.count(j) > max_cap:
            if female.count(j) % max_cap > 0:
                ans += 1
                ans += female.count(j) // max_cap
            else:
                ans += female.count(j) // max_cap
    if male.count(j) > 0:
        if male.count(j) <= max_cap:
            ans += 1
        elif male.count(j) > max_cap:
            if male.count(j) % max_cap > 0:
                ans += 1
                ans += male.count(j) // max_cap
            else:
                ans += male.count(j) // max_cap
print(ans)