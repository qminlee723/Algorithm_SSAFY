V = int(input())
vote = input()

a = vote.count('A')
b = vote.count('B')

if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')