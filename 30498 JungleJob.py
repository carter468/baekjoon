# Jungle Job
# Platinum 3, DP, DP_tree

import sys
input = sys.stdin.readline
sys.setrecursionlimit(9999)
MOD = 10**9+7

def dfs(x):
    cur = [0,1]
    size = 1
    for nx in children[x]:
        dfs(nx)
        c = subtree_size[nx]
        nxt = [0]*(size+c+1)
        for s in range(1,size+1):
            nxt[s] = (nxt[s]+cur[s])%MOD
            if cur[s] != 0:
                for t in range(1,c+1):
                    nxt[s+t] = (nxt[s+t]+cur[s]*dp[nx][t])%MOD
        size += c
        cur = nxt
    dp[x] = cur
    subtree_size[x] = size

N = int(input())
parents = [0]*N
children = [[] for _ in range(N)]
for i in range(1,N):
    p = int(input())
    parents[i] = p
    children[p].append(i)

subtree_size = [0]*N
dp = [None]*N

dfs(0)

result = [0]*(N+1)
for i in range(N):
    for k in range(1,len(dp[i])):
        result[k] = (result[k]+dp[i][k])%MOD

print(*result[1:],sep='\n')