# A+를 향하여
# Gold 2, knapsack, binary search

import sys
input = sys.stdin.readline

def check(x):
    m = T-x
    dp = [0]*(m+1)
    for t,w in A:
        t = max(0,t-x)
        for i in range(m,t-1,-1):
            dp[i] = max(dp[i],dp[i-t]+w)
    return max(dp) >= W

N,T,W = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(N)]

no,yes = -1,T+1
while no+1 < yes:
    mid = (no+yes)//2
    if check(mid): yes = mid
    else: no = mid
print(yes if yes < T+1 else -1)