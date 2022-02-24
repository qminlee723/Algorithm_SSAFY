import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    deck = input().split()

    split_deck = []
    for i in range(n//2):
        split_deck.append(deck.pop())
        split_deck.sort(reverse=False)

    deck_final = [0] * n
    for j in range(n, 2):
        deck_final.append(deck)
