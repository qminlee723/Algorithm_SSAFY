import sys
sys.stdin = open('input.txt')

dwarf_height = []
for _ in range(9):
    dwarf_height.append(int(input()))

sum_height = sum(dwarf_height)
fake_dwarf = sum_height - 100

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        elif dwarf_height[i] + dwarf_height[j] == fake_dwarf:
            a = dwarf_height[j]
            b = dwarf_height[i]
            break
dwarf_height.remove(a)
dwarf_height.remove(b)

dwarf_height.sort()
for k in dwarf_height:
    print(k)