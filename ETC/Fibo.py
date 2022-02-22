
# 1
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(10))


# 2
def fibo_memo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo_memo(n - 1) + fibo_memo(n - 2))
    return memo[n]


memo = [0, 1]

print(fibo_memo(10))