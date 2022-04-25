import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())

# 최대공약수 구하는 함수
# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 = a * b // 최대공약수
def lcm(a, b):
    return a * b // gcd(a, b)

gcd_num = gcd(a,b)
lcm_num = lcm(a,b)

print(gcd_num)
print(lcm_num)
