# 안 보고 정렬
# Gold 2, combinatorics, inclusion and exclusion

import sys
input = sys.stdin.readline
MOD = 998244353

for _ in range(int(input())):
    N,L,R = map(int,input().split())
    x = R-L+1
    if L == R: print(1)
    else: print((pow(x,N,MOD)-pow(x-1,N,MOD)*2+pow(x-2,N,MOD))%MOD)