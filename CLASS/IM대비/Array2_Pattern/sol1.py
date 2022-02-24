
map = [["A","B","G","K"],["T","T","A","B"],["A","C","C","D"]]
input = [list(input()) for _ in range(2)]

def is_pattern(y, x):
    for i in range(2):
        for j in range(2):
            if 