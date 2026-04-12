# 방문 판매 (Hard)
# Platinum 4, DP, topological sorting

import sys
input = sys.stdin.readline
INF = 10**9

N,M,X,Y = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    graph[a].append(b)
    indegree[b] += 1
A = [tuple(map(int,input().split())) for _ in range(N)]

q = []
for i in range(N):
    if indegree[i] == 0:
        q.append(i)

result = INF,0
dp = [[-INF]*(X+1) for _ in range(N+1)] # n명 구매, X제품을 x만큼 구매 했을때 Y제품의 최대구매양
dp[0][0] = 0
count = 0
while q:
    count += len(q)
    nq = []
    for i in sorted(q):
        a,b = A[i]
        ndp = [[-INF]*(X+1) for _ in range(N+1)]
        for n in range(count):
            for x in range(X+1):
                ndp[n][x] = max(ndp[n][x],dp[n][x])
                nx = min(X,x+a)
                ndp[n+1][nx] = max(ndp[n+1][nx],dp[n][x]+b)
                if nx == X and ndp[n+1][nx] >= Y and n+1 < result[0]:
                    result = n+1,i+1
        dp = ndp

        for j in graph[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                nq.append(j)
    q = nq

if count < N or result[0] > N: print(-1)
else: print(*result,sep='\n')