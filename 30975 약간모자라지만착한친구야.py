# 약간 모자라지만 착한 친구야
# Platinum 5, DP, TSP

INF = 10**9

def solve(u,s):
    if dp[u][s] != -1: return dp[u][s]
    if s+1 == 1<<N: return dist[u][N]

    dp[u][s] = INF
    for v in range(N):
        if s>>v&1 == 0 and (P[v]-1 == v or s>>(P[v]-1)&1 == 1):
            dp[u][s] = min(dp[u][s],solve(v,s|(1<<v))+dist[u][v])
    return dp[u][s]

N,M = map(int,input().split())
P = tuple(map(int,input().split()))
dist = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    u,v = u-1,v-1
    dist[u][v] = min(dist[u][v],w)

dp = [[-1]*(1<<N) for _ in range(N+1)]
d = solve(N,0)
print(d if d < INF else -1)