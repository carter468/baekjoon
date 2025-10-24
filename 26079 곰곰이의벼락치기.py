# 곰곰이의 벼락치기
# Platinum 4, DP, combinatorics, modular multiplicative inverse

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MOD = 10**9+7

def nCr(n,r):
    return fac[n]*ifac[r]*ifac[n-r]%MOD

def solve(x):
    if dp[x]: return dp[x]

    dp[x] = [1,1]
    for nx in graph[x]:
        solve(nx)
        dp[x][0] = dp[x][0]*dp[nx][0]%MOD
        dp[x][1] += dp[nx][1]

    a = 1
    n = dp[x][1]-1
    for nx in graph[x]:
        a = a*nCr(n,dp[nx][1])
        n -= dp[nx][1]
    dp[x][0] = dp[x][0]*a%MOD

    return dp[x]

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

fac = [1]
for i in range(N):
    fac.append(fac[-1]*(i+1)%MOD)
ifac = [pow(fac[-1],-1,MOD)]
for i in range(N):
    ifac.append(ifac[-1]*(N-i)%MOD)
ifac.reverse()

dp = [None]*(N+1)
result = 1
for i in range(1,N+1):
    if indegree[i] == 0:
        solve(i)
        result = result*dp[i][0]*nCr(N,dp[i][1])%MOD
        N -= dp[i][1]
print(result)