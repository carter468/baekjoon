# 2K-Flip
# Gold 3, prefix sum, combinatorics

import sys
input = sys.stdin.readline
MOD = 998244353

N,K = map(int,input().split())
A = tuple(map(int,input().split()))
count = [0]*(N+1)
for _ in range(K):
    l,r = map(int,input().split())
    count[l-1] += 1
    count[r] -= 1
for i in range(N):
    count[i+1] += count[i]

result = 0
for i in range(N):
    k = count[i]
    if k > 0:
        result += pow(2,k-1,MOD)*pow(2,K-k,MOD)
    elif A[i] == 1:
        result += pow(2,K,MOD)
print(result%MOD)