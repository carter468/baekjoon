# 교차 집합 크기 합
# Platinum 4, combinatorics, modular multiplicative inverse

from collections import defaultdict
import sys
input = sys.stdin.readline
MOD = 998244353
MAX = 10**6

N = int(input())
count = defaultdict(int)
for _ in range(N):
    for a in tuple(map(int,input().split()))[1:]:
        count[a] += 1

fact = [1]*(MAX+1)
for i in range(1,MAX+1):
    fact[i] = fact[i-1]*i%MOD
rfact = [1]*(MAX+1)
rfact[MAX] = pow(fact[MAX],-1,MOD)
for i in range(MAX-1,0,-1):
    rfact[i] = rfact[i+1]*(i+1)%MOD

result = [0]*(N+1)
for x in count:
    i = count[x]
    for j in range(1,i+1):
        result[j] = (result[j]+fact[i]*rfact[j]*rfact[i-j])%MOD

print(*result[1:],sep='\n')