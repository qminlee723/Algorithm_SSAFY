import sys

sys.stdin = open('input.txt')
#
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    receipt = list(map(int, input().split()))

    discount = []
    for i in range(len(receipt)//2):
        price = receipt.pop()
        if price * 3 // 4 in receipt:
            discount.append(price * 3 // 4)
            receipt.remove(price * 3 // 4)
    rlt = sorted(discount)

    print(f'Case #{tc}: {" ".join(map(str, rlt))}')