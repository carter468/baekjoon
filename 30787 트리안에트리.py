# 트리 안에 트리
# Gold 3, math, combinatorics

M = 10**9+7

n,k = map(int,input().split())

result = 1
t = 1
p = 2
for i in range(n-k):
    if i == k-1: t = 3
    result = (result+p*t)%M
    p *= 2

print(result)