# 트리 뒤집기
# Gold 1, DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

def solve(x,s,p):
    if dp[x][s] != INF: return dp[x][s]

    if s == 0:
        a,b = F[x],B[x]
    else:
        a,b = B[x],F[x]

    if a > b:
        dp[x][s] = 0
        for nx in graph[x]:
            if nx != p:
                dp[x][s] += solve(nx,s,x)
        return dp[x][s]
    elif a < b:
        dp[x][s] = 1
        for nx in graph[x]:
            if nx != p:
                dp[x][s] += solve(nx,1-s,x)
        return dp[x][s]
    else:
        r1 = 0
        for nx in graph[x]:
            if nx != p:
                r1 += solve(nx,s,x)
        r2 = 1
        for nx in graph[x]:
            if nx != p:
                r2 += solve(nx,1-s,x)
        dp[x][s] = min(r1,r2)
        return dp[x][s]

N = int(input())
F = [0]+list(map(int,input().split()))
B = [0]+list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
for i in range(1,N+1):
    result += max(F[i],B[i])

dp = [[INF,INF] for _ in range(N+1)]
print(result,solve(1,0,0))