# 떡파이어
# Gold 5, math, exponentiation by squaring

def pow(x):
    if x == 1: return 2
    a = pow(x//2)
    if x%2 == 0: return a*a%M
    else: return a*a*2%M

M = 10**9+7

n = int(input())
print(1 if n < 2 else pow(n-1))