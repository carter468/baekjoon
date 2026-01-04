# Longest Common Path
# Platinum 5, DP, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x,p):
    global result
    if dp[x]: return dp[x]
    
    arr = []
    for nx in graph1[x]:
        if nx != p:
            r = solve(nx,x)
            if nx in graph2[x]:
                arr.append(r)
    arr.sort()
    if len(arr) >= 2:
        a,b = arr[-1]
        c,d = arr[-2]
        if a+c > result[0]:
            result = (a+c,b,d)
        dp[x] = (a+1,b)
    elif arr:
        a,b = arr[-1]
        if a+1 > result[0]:
            result = (a+1,b,x)
        dp[x] = (a+1,b)
    else:
        dp[x] = (1,x)
    return dp[x]

N = int(input())
graph1 = [set() for _ in range(N+1)]
graph2 = [set() for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph1[u].add(v)
    graph1[v].add(u)
for _ in range(N-1):
    u,v = map(int,input().split())
    graph2[u].add(v)
    graph2[v].add(u)

dp = [None]*(N+1)
result = (1,0,0)
solve(1,0)

if result[0] == 1: print(-1)
else: print(*result[1:])