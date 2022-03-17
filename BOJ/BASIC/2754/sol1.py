letter = input()
grade = 0

if 'A' in letter:
    grade = 4
elif 'B' in letter:
    grade = 3
elif 'C' in letter:
    grade = 2
elif 'D' in letter:
    grade = 1
elif 'F' in letter:
    grade = 0

if '+' in letter:
    grade += 0.3
elif '0' in letter:
    grade += 0.0
elif '-' in letter:
    grade -= 0.3

print(float(grade))