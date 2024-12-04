# 섬 여행
# Gold 3, DP

import sys
input = sys.stdin.readline

def solve(x,c):
    if dp[x][c] != 11111: return dp[x][c]
    if c == 0: return H[x-1]

    for nx in graph[x]:
        dp[x][c] = min(dp[x][c],solve(nx,c-1))
    
    return dp[x][c]

N,M = map(int,input().split())
H = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dp = [[11111]*501 for _ in range(N+1)]
for i in range(1,N+1):
    solve(i,500)

for _ in range(int(input())):
    a,k = map(int,input().split())
    print(dp[a][k] if dp[a][k] != 11111 else -1)